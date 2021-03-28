class Stopwatch:
    def __init__(self, screen, color, font):
        self.screen = screen
        self.text_color = color
        self.base_font = font
        self.startTimer = 0  # first time stamp
        self.endTimer = 0  # Always updating 
        self.deltaTime = 0
        # self.pos_x = 0
        # self.pos_y = 0

    def updateTimer(self):

        # Reset show time to 0, by taking the current tick and subtract it by the previous time stamp
        timer_value = self.endTimer - self.startTimer
        timer = self.base_font.render("Time : " + str(timer_value/1000), True, self.text_color)
        timer_rect = timer.get_rect(center=(400, 20))
        self.screen.blit(timer, timer_rect)