import telnetlib

try:
    t = telnetlib.Telnet('localhost')
    
    t.read_until('login:')
    t.write('adminku\n')
    t.read_until('assword:') # let "p" be capitalized or not
    t.write('mypass\n')
    n, match, previous_text = t.expect([r'Login Incorrect', r'\$', 10])
    
    if n == 0:
        print("Username & Password Gagal")
    else:
        t.write('exec uptime\n')
        print(t.read_all())
except:
    print("Gagal Bosku")