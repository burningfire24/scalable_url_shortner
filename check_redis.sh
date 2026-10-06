
CONTAINER="redis1"

docker exec -i "$CONTAINER" redis-cli KEYS "*" | while read -r key; do
  key=$(echo "$key" | tr -d '\r')
  type=$(docker exec -i "$CONTAINER" redis-cli TYPE "$key" | tr -d '\r')

  echo -n "Key: $key (Type: $type) => Value: "

  case "$type" in
    string)
      docker exec -i "$CONTAINER" redis-cli GET "$key"
      ;;
    hash)
      docker exec -i "$CONTAINER" redis-cli HGETALL "$key"
      ;;
    list)
      docker exec -i "$CONTAINER" redis-cli LRANGE "$key" 0 -1
      ;;
    set)
      docker exec -i "$CONTAINER" redis-cli SMEMBERS "$key"
      ;;
    zset)
      docker exec -i "$CONTAINER" redis-cli ZRANGE "$key" 0 -1 WITHSCORES
      ;;
    *)
      echo "(Unsupported type: $type)"
      ;;
  esac
done
