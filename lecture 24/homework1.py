from abc import ABC, abstractmethod
class AppFuncs(ABC):
    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def pause(self):
        pass
    
    @abstractmethod
    def next(self):
        pass

class FastForward(ABC):
    @abstractmethod
    def fast_forward(self):
        pass

class Stop(ABC):
    @abstractmethod
    def stop(self):
        pass



class VideoPlayer(AppFuncs, FastForward):
    def play(self):
        print("Playing video")

    def pause(self):
        print("Pausing video")

    def next(self):
        print("Next video")

    def fast_forward(self):
        print("Fast forwarding")

class StreamingPlayer(AppFuncs):
    def __init__(self, video_player: FastForward):
        self.video_player = video_player
    
    def play(self):
        print("Playing video")

    def pause(self):
        print("Pausing video")

    def next(self):
        print("Next video")

    def fast_forward(self):
        print("Fast forwarding")
    
    def forward(self):
        self.video_player.fast_forward()

class AudioPlayer(AppFuncs, Stop):
    def play(self):
        print("Playing audio")

    def pause(self):
        print("Pausing audio")

    def next(self):
        print("Next audio")

    def stop(self):
        print("Stopping audio")



video_player = VideoPlayer()
streaming_player = StreamingPlayer(video_player)
streaming_player.forward()















