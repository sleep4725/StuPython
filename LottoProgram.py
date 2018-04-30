import random as rd
import pprint as ppr
class Lotto:
    # 생성자
    def __init__(self):
        self.Total_number = [x for x in range(1, 46)] # 1,2,3,4, ..., 45
        self.Me_R_Lott = list()
        self.Me_C_Lott = None
        self.TodayLotto = list()
        self.BonusNumber = 0
        self.LottoResult = dict()
        self.choiceDict = {'Random':'n', 'Choice':'n'}
        self.MeLottoInformation = {'Random':None,
                                   'Choice':None}
    def TodayLottoSetting(self):
        self.TodayLotto = rd.sample(self.Total_number, 7)
        tmp_choice_bounce_index = rd.randint(0, len(self.TodayLotto)-1)

        # 보너스 번호 선택
        self.BonusNumber = self.TodayLotto[tmp_choice_bounce_index]
        self.TodayLotto.remove(self.BonusNumber)

        # 오름차순으로 정렬
        self.TodayLotto.sort()
        print ("오늘의 당첨 번호 및 보너스 번호========================")
        print (self.TodayLotto , " + " , self.BonusNumber)
        print ("======================================================")

    def SelectLotto(self):
        while True:
            try:
                choice = input("랜덤으로 진행하시겠습니까?(n(N)/y(Y))").lower()
            except:
                print ("문자를 입력해주세요")
            else:
                if choice != 'n' and choice != 'y':
                    print ("아씨!! n 또는 y만 입력해달라고 !!!!")
                else: # choice == 'n' or choice == 'y':
                    if choice == 'y':
                        self.choiceDict['Random'] = 'y'
                        #meLottoObject.RandomLottoSetting()
                        try:
                            choice = input("수동으로 진행하시겠습니까?(n(N)/y(Y))").lower()
                        except:
                            print ("문자를 입력해주세요")
                        else:
                            if choice != 'n' and choice != 'y':
                                print ("아씨!! n 또는 y만 입력해달라고 !!!!")
                            else: # choice == 'n' or choice == 'y':
                                if choice == 'n': # case 1) 랜덤으로도 수동으로도 하지 않는 경우
                                    break
                                else: # choice == 'y'
                                    #meLottoObject.ChoiceLottoSetting()
                                    self.choiceDict['Choice'] = 'y'
                                    break
                    else: # choice == 'n':
                        try:
                            choice = input("수동으로 진행하시겠습니까?(n(N)/y(Y))").lower()
                        except:
                            print ("문자를 입력해주세요")
                        else:
                            if choice != 'n' and choice != 'y':
                                print ("아씨!! n 또는 y만 입력해달라고 !!!!")
                            else: # choice == 'n' or choice == 'y':
                                if choice == 'n': # case 1) 랜덤으로도 수동으로도 하지 않는 경우
                                    print ("뭐야 안 할꺼면서 프로그램 왜 돌린거야 쳇")
                                    break
                                else: # choice == 'y'
                                    #meLottoObject.ChoiceLottoSetting()
                                    self.choiceDict['Choice'] = 'y'
                                    break
    """랜덤으로 선택하는 경우"""
    def RandomLottoSetting(self):
        cntLotto = int(input("랜덤으로 몇 번 할래?: "))
        for _ in range(cntLotto):
            tmp_lotto_ball = rd.sample(self.Total_number, 6)
            tmp_lotto_ball.sort() # 오름차순으로 정렬
            self.Me_R_Lott.append(tmp_lotto_ball)
        self.MeLottoInformation['Random'] = self.Me_R_Lott
        ppr.pprint (self.MeLottoInformation['Random'])

    """직접 선택하는 경우"""
    def ChoiceLottoSetting(self):
        cntLotto = int(input("수동으로 몇 번 할래?: "))
        self.Me_C_Lott = [[0 for _ in range(6)] for _ in range(cntLotto)]
        print (self.Me_C_Lott)
        for i in range(len(self.Me_C_Lott)):
            for j in range(0, len(self.Me_C_Lott[i])):
                while True:
                    promptValue = str(j+1) + "번째 볼 입력: "
                    try:
                        self.Me_C_Lott[i][j] = int(input(promptValue))
                    except:
                        print ("숫자를 입력해주셔야 합니다.")
                    else:
                        if self.Me_C_Lott[i][j] <= 0 or self.Me_C_Lott[i][j] > 45:
                            print ("반드시 1에서 부터 45사이의 값을 입력하셔야 합니다.")
                        else: # 1 <= self.Me_C_Lott[i] <= 45
                            if self.Me_C_Lott[i][j] in self.Me_C_Lott[i][:j]:
                                print ("중복되는 값이 존재합니다. 다시 입력해주세요")
                            else: # self.Me_C_Lott[i][j] not in self.Me_C_Lott[i]
                                break

            # 입력받은 로또 오름차순으로 정렬
            self.Me_C_Lott[i].sort()
            print ("입력하신 로또 번호 입니다. : {}".format(self.Me_C_Lott[i][:]))
        self.MeLottoInformation['Choice'] = self.Me_C_Lott
        ppr.pprint (self.MeLottoInformation['Choice'])

    def LottoGrade(self):
        # 최소 한개 이상의 랜덤 로또의 갯수가 있다면
        """
            3개면 "5등"
            4개면 "4등"
            5개면 "3등"
            5개 + 보너스 "2등"
            6개면 "1등"
        """
        for k in ['Random', 'Choice']:
            if self.MeLottoInformation[k] != None:
                for j in range(0, len(self.MeLottoInformation['Random'])):
                    cnt = 0
                    for i in self.TodayLotto:
                        if i in self.MeLottoInformation['Random'][j]:
                            cnt += 1
                    print (self.MeLottoInformation['Random'][j], end=" ")
                    if cnt < 3:
                        print ("꽝")
                    else: # cnt >= 3
                        if cnt == 3:
                            print ("5등")
                        elif cnt == 4:
                            print ("4등")
                        elif cnt == 5:
                            if self.BonusNumber in self.MeLottoInformation['Random'][j]:
                                print ("2등")
                            else:
                                print ("3등")
                        else:
                            print ("1등")

def main():
    meLottoObject = Lotto() # 객체 생성
    meLottoObject.TodayLottoSetting()
    meLottoObject.SelectLotto()

    if meLottoObject.choiceDict['Random'] == 'y' or meLottoObject.choiceDict['Choice'] == 'y':
        if meLottoObject.choiceDict['Random'] == 'y':
            meLottoObject.RandomLottoSetting()
        if meLottoObject.choiceDict['Choice'] == 'y':
            meLottoObject.ChoiceLottoSetting()
        meLottoObject.LottoGrade()
    else:
        print ("인생 역전은 다음 기회에 노려보라고")
if __name__ == "__main__":
    main()
