class PreviousList:
    def __init__(self, screen, font, previous):
        self.screen = screen
        self.base_font = font
        self.previous = previous
        self.pos_x = 0
        self.pos_y = 60
        self.correct = (66, 245, 147)
        self.wrong = (245, 99, 66)

    def updatepreviousList(self):

        # Iterate each item in the history
        for i in self.previous:

            # If True (Correct)
            if i[3] == True:

                # Render Answer_Question_Time with correct color
                a_q_t = self.base_font.render(str(i[0]) + " " + str(i[1]) + "   " + str(i[2]), True, self.correct)
                self.screen.blit(a_q_t, (self.pos_x, i[-1]))

            else:

                # Render Answer_Question_Time with correct color
                a_q_t = self.base_font.render(str(i[0]) + " " + str(i[1]) + "   " + str(i[2]), True, self.wrong)
                self.screen.blit(a_q_t, (self.pos_x, i[-1]))


    def moveDown(self):

        # Append current list position by +20
        self.pos_y += 20
        self.previous[-1].append(self.pos_y)
        

    