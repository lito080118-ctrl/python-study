class Board:
    def set_data(self,title, writer): #책제목, 저자 저장
        self.title = title #오른쪽 title은 호출할때 받아온 메개변수값
        self.writer = writer
        self.cnt =0

    def cntup(self):
        self.cnt +=1


#게시판 객체 생성
    # Board board1 = new Board() 자바
board1 = Board() #객체변수=클래스(메개변수)
board2 = Board()
board1.set_data("자바의 정석","홍길동")
board2.set_data("파이썬 정석","이순신")

board1.cntup()
board1.cntup()
board2.cntup()
print(board1.title,board1.writer,board1.cnt)
print(board2.title,board2.writer,board2.cnt)

board3= Board()
#