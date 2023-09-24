maxhp=360
maxmp=1180
novamp=400
recoverlyline1=100
recoverlyamout=100
novadamege=600
recoverlymp=500
tarn=1
#変数の定義
n1hp =maxhp
n1mp =maxmp
n2hp =maxhp
n2mp =maxmp
recoverlyline2=novadamege
#数値設定
print('バトル開始')
#スーパーノヴァ、リカバリーショット、リセット
while n1hp > 0 or n2hp > 0:
    print(tarn)
    print('n1のターン')
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
#第一人目スキル選択
    print('n1の')
    print(n1skill)
    print('が発動')
    if n1skill == 'スーパーノヴァ':
        n2hp =- novadamege
        n1mp =- novamp
        print('n2に')
        print(novadamege)
        print('のダメージ')
    #スーパーノヴァ
    elif n1skill == 'リカバリーショット':
        n1hp += recoverlyamout
        n1mp =- recoverlymp
        print('n1は')
        print(recoverlyamout)
        print('回復')
    #リカバリーショット
    elif n1skill == 'リセット':
        n1mp = maxmp
        print('n1のMPが最大まで回復した')
#n1のターン終わり


    print('n2のターン')
    if n2hp >= recoverlyline1:
        if n2mp >= novamp:
            n2skill='スーパーノヴァ'
        else:
            n2skill='リセット'
    else:
        if n2mp >= recoverlymp:
            n2skill='リカバリーショット'
        else:
            if n1hp <= recoverlyline2:
                if n2mp >= novamp:
                    n2skill='スーパーノヴァ'
                else:
                    n2skill='リセット'
            else:
                n2skill='リセット'
#第2人目スキル選択
    print('n2の')
    print(n2skill)
    print('が発動')
    if n2skill == 'スーパーノヴァ':
        n1hp =-novadamege
        n2mp =- novamp
        print('n1に')
        print(novadamege)
        print('のダメージ')
    #スーパーノヴァ
    elif n2skill == 'リカバリーショット':
        n2hp += recoverlyamout
        n2mp += recoverlymp
        print('n2は')
        print(recoverlyamout)
        print('回復')
    #リカバリーショット
    elif n2skill == 'リセット':
        n2mp = maxmp
        print('n2のMPが最大まで回復した')
#n2のターン終わり
    tarn += 1
    if tarn == 10000:
        break
if n2hp <=0:
    print('n1の勝利')
elif n1hp<=0:
    print('n2の勝利')
elif tarn == 10000:
    print('規定ターンに達しました。')
else:
    print('エラー')

#最後に回復する問題の修正から