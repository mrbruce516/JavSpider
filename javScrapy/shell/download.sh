cat /data/scrapy/scrapyd/scrapyd/data/`date +%Y-%m-%d`.magnet.txt | xargs -n 1 -P 5 -I {} curl -s -X POST \
    --header 'Content-Type: application/json' \
    --data '{"jsonrpc": "2.0", "method": "aria2.addUri", "id": "1", "params": ["token:mrbruce516",["{}"],{"dir":"/downloads/av"}]}' \
    http://127.0.0.1:6800/jsonrpc
