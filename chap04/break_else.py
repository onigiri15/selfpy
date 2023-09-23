data = ['さくら', 'うめ', '×', 'くちなし', 'ぼたん']	
# data = ['さくら', 'うめ', '×', 'くちなし', 'ぼたん']

for name in data:
  if name == '×':
      break
  print(name)
else:
  print('正常終了しました。')