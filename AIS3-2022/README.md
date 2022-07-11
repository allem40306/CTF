# Write Up

- BOF2WIN
    - 用逆向工具得出輸入多少字元會改變 rip 和 get_the_flag 的位置，再利用
pwntool 解題。
- Excel
    - 打開 excel 工具，使用巨集工具，一直執行直到出現 flag。
- Fast Cipher 
    - 發現 key 後面會固定成 163，找出前面非 163 的值，接者將加密的文件依照
XOR 的值解密回去就得到 flag。
- Gift in the dream
    - 利用 identify 工具發現每一禎的時間剛好是 ASCII 的值，把 ASCII 還原成字元
就拿到 flag。
- Poking Bear
    - 發現每隻熊有不同的 ID，用 python 的 request 和 bs4 套件找出隱藏熊的
ID，接著將 cookie 的值從 human 改成 Poking Bear 並送出請求，就可以得到
flag。
- SAAS – Crash
    - 插入一個空字串，查詢兩次。
- SC
    - 利用 cipher.py 和 cipher.py.enc 的對應關係將 flag.txt.enc 還原得到 flag
- Time Management (AIS3{You_are_the_master_of_time_management!!!!!})
    - 利用逆向工具程式發現執行到 sleep 函式會卡住，因此用 GDB debug 模式，遇到 sleep 函式就改變目前執行的地址，flag 就會顯示。
- Welcome
    - 看 discord。