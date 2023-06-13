#!usr/bin/env python
# -*- coding: utf-8 -*-
# author: kuangdd
# date: 2019/12/1
"""
local
"""
import logging
import pdb



logging.basicConfig(level=logging.INFO)

result_name = "/storage/pooh/AISHELL3/test/txt/SSB0006_content.txt"
path = "/storage/pooh/AISHELL3/test/wav/temp_data/SSB0006/SSB0006_text-file"

def run_text2phoneme():
    from phkit.chinese.sequence import text2phoneme, text2sequence
    import os

    # 读文件
    files = os.listdir(path=path)

    files.sort()

    # 写文件
    result_file = open(result_name, "w")

    for file in files:
        f = open(path + "/" + file)
        iter_f = iter(f)
        content = "/storage/pooh/AISHELL3/test/wav/SSB0006/" + file[:11] + ".wav" + "|sil"
        text = ""
        for line in iter_f:
            text = text + line
        
        out = text2phoneme(text)

        # 从一个out list转化为content str
        for i in range(len(out)):
            if out[i] >= '0' and out[i] <= '9':
                content = content + out[i]
            elif out[i] == "、" or out[i] == ";" or out[i] == ":" or out[i] == "," or out[i] == "。" or out[i] == "." or out[i] == "?" or out[i] == "!":
                del out[i+1]
                continue
            else:
                content = content + " " + out[i]
                if out[i] == "sil eos":
                    content = content + "\n"
                    break
        
        # 写入
        result_file.write(content)

    result_file.close()
        
    
  

if __name__ == "__main__":
    run_text2phoneme()
