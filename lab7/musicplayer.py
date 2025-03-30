import pygame
import keyboard
import time
import os


music_folder = r'D:\codes\PP2\lab7\music_player_songs'
playlist = [song for song in os.listdir(music_folder) if os.path.isfile(os.path.join(music_folder, song))]
full_paths = [os.path.join(music_folder, song) for song in playlist]


class got_it:
    def __init__(self):
        self.playlist = full_paths
        self.cur_index = 0
        self.is_playing = False
        self.paused_time_s = 0
        self.paused_time_m = 0
        self.paused = False

        pygame.mixer.init()

    def play_song(self):
        if not self.is_playing:
            if self.paused:
                pygame.mixer.music.unpause()
                print("Resume:", self.playlist[self.cur_index], "from", self.paused_time_m, ":", self.paused_time_s)
            else:
                pygame.mixer.music.load(self.playlist[self.cur_index])
                pygame.mixer.music.play()
                print("Playing:", self.playlist[self.cur_index])
            self.is_playing = True
            self.paused = False
            
    def stop_song(self):
        if self.is_playing:
            pygame.mixer.music.stop()
            print("Stopped:", self.playlist[self.cur_index])
            self.is_playing = False
            self.paused = False
    
    def pause_song(self):
        if self.is_playing and not self.paused:
            self.paused_time_s = int(pygame.mixer.music.get_pos() / 1000) % 60
            self.paused_time_m = int(pygame.mixer.music.get_pos() / 60000) % 60
        pygame.mixer.music.pause()
        print(f"Paused: {self.playlist[self.cur_index]} at {self.paused_time_m}:{self.paused_time_s}")
        self.paused = True
    
    def resume_song(self):
        if self.is_playing and self.paused:
            pygame.mixer.music.unpause()
            print(f"Resuming: {self.playlist[self.cur_index]} from {self.paused_time_m}:{self.paused_time_s}")
            self.paused = False

    def next_song(self):
        self.stop_song()
        self.cur_index = (self.cur_index + 1) % len(self.playlist)
        self.play_song()
    
    def prev_song(self):
        self.stop_song()
        self.cur_index = (self.cur_index - 1) % len(self.playlist)
        self.play_song()
    
def main():
    player = got_it()
    keyboard.add_hotkey('p', player.play_song)
    keyboard.add_hotkey('s', player.stop_song)
    keyboard.add_hotkey('space', player.pause_song)
    keyboard.add_hotkey('r', player.resume_song)
    keyboard.add_hotkey('b', player.prev_song)
    keyboard.add_hotkey('n', player.next_song)

    print("Press 'p' to play, 's' to stop, 'space' to pause, 'r' to resume, 'n' for next song, 'b' for previous song, 'q' to quit")

    while True:
        if keyboard.is_pressed('q'):
            pygame.mixer.quit()
            break
        time.sleep(0.1)

if __name__ == "__main__":
    main()




