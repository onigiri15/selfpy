import re

msg = '<p>サポートサイト<a href="https://www.wings.msn.to/">https://www.wings.msn.to/</a></p>'
ptn = re.compile(r'<a href="(.+?)">\1</a>')
results = ptn.finditer(msg)
for result in results:
  print(result.group())