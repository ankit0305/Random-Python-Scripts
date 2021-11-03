#works on your personal server. Not meant for production.
import speedtest

s = speedtest.Speedtest()
s.get_best_server(s.set_mini_server("YOUR SERVER"))
s.download()