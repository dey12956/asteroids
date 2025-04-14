import pygame

def load_explosion_frames(sheet, frame_width=32, frame_height=32, num_frames=6):
    frames = []
    for i in range(num_frames):
        frame = sheet.subsurface(pygame.Rect(
            i * frame_width, 0, frame_width, frame_height
        ))
        frames.append(frame)
    return frames