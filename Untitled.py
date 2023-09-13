#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pygame


# In[2]:


import pygame

# Initialize pygame
pygame.mixer.init()

# Set the absolute path to your music file (copy from your file explorer)
music_file = r'Kanhaiya Twitter Pe Aaja The Great Indian Family 320 Kbps.mp3'

try:
    # Load the music file
    pygame.mixer.music.load(music_file)

    # Play the music
    pygame.mixer.music.play()

    while True:
        # Check for user input or some other condition to stop the music
        user_input = input("Press 's' to stop the music: ")
        if user_input.lower() == 's':
            pygame.mixer.music.stop()
            break

except pygame.error as e:
    print(f"An error occurred: {e}")


# In[ ]:





# In[ ]:




