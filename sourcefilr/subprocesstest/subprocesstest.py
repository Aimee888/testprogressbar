import subprocess


def Func():
    p = subprocess.Popen("python testhello.py", stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    try:
        p.wait(timeout=10)
    except Exception as e:
        print("===== process timeout ======")
        p.kill()
        return None
    output = p.communicate()[0]
    err = p.communicate()[1]
    print(output)
    print(p.returncode)


if __name__ == "__main__":
    Func()
