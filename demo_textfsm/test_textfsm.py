import textfsm
from textfsm import TextFSM

traceroute = '''
<R1>tracert 192.5.5.5
tracert 192.5.5.5
 traceroute to  192.5.5.5(192.5.5.5), max hops: 30 ,packet length: 40,press CTRL_C to break 
 1 36.1.1.6 60 ms  50 ms  10 ms 
 2 67.1.1.7 100 ms  90 ms  80 ms 
 3 78.1.1.8 90 ms  80 ms  60 ms 
 4 59.1.1.9 100 ms  90 ms  80 ms 
 5 59.1.1.5 90 ms  100 ms  60 ms
'''
with open('traceroute.template') as template:
    fsm = textfsm.TextFSM(template)
    result = fsm.ParseText(traceroute)
    print(fsm.header)
    print(result)


def show_version_sample():
    with open("show_version_sample", "r", encoding="utf8") as f:
        dev_text = f.read()
    template_1 = TextFSM(open("show_version_sample.template"))
    version_info = template_1.ParseTextToDicts(dev_text)
    print(version_info)


if __name__ == '__main__':
    show_version_sample()