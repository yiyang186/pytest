import subprocess


def run():
  cmd = 'python backend.py'
 p = subprocess.Popen(cmd,
                       shell=True,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)

  while True:
    out, err = p.communicate()
    print(out)


if __name__ == '__main__':
  run()
