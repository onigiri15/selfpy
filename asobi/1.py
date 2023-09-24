maxhp=360
maxmp=780
novamp=79
recoverlyline1=200
novadamege=179
recoverlymp=200
#変数の定義
n1hp =maxhp
n1mp =maxmp
n2hp =maxhp
n2mp =maxmp
recoverlyline2=novadamege
#数値設定
print(maxhp)
print('バトル開始')
#スーパーノヴァ、リカバリーショット、リセット
if n1hp >= recoverlyline1:
    if n1mp >= novamp:
        n1skill='スーパーノヴァ'
    else:
        n1skill='リセット'
else:
    if n1mp >= recoverlymp:
        n1skill='リカバリーショット'
    else:
        if n2hp <= recoverlyline2:
            if n1mp >= novamp:
                n1skill='スーパーノヴァ'
            else:
                n1skill='リセット'
        else:
            n1skill='リセット'

print(n1skill)
