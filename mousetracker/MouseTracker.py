import ctypes

class MouseTracker:
    def __init__(self, dll_path="./mousetracker/MouseTracker.dll"):
        self._dll = ctypes.CDLL(dll_path)
    
    def start(self):
        self._dll.startMouseTracking()

    def stop(self):
        self._dll.stopMouseTracking()

    def get_deltas(self):
        deltaX = self._dll.getAccumulatedDeltaX()
        deltaY = self._dll.getAccumulatedDeltaY()
        return deltaX, deltaY

    def is_button_pressed(self, button_name):
        if button_name == "left":
            return self._dll.isLeftButtonDown()
        elif button_name == "right":
            return self._dll.isRightButtonDown()
        elif button_name == "middle":
            return self._dll.isMiddleButtonDown()
        elif button_name == "x1":
            return self._dll.isXButton1Down()
        elif button_name == "x2":
            return self._dll.isXButton2Down()
        return False
        raise Exception("invalid mouse button selected")

    def get_scroll_count(self):
        return self._dll.getAccumulatedScroll()

    def __del__(self):
        self.stop()

if __name__ == "__main__":
    import time
    mt = MouseTracker("./MouseTracker.dll")
    mt.start()
    while True:
        time.sleep(1)
        print(mt.get_deltas())
        print(mt.is_button_pressed('left'))
        print(mt.get_scroll_count())
    mt.stop()
