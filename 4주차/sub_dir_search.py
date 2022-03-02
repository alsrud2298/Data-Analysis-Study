# 하위 디렉토리 검색하기
# 특정 디렉토리부터 시작해 그 하위 파일 중 파이썬 파일만 출력하는 프로그램

import os
def search(dirname):
    try: 
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == ".py":
                    print(full_filename)
    except PermissionError:
        pass
    
search("c:/")

# os.walk : 시작 디렉토리부터 하위 모든 디렉토리 차례로 방문
for (path, dir, files) in os.walk("c:/"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.py':
            print("%s/%s" % (path, filename))