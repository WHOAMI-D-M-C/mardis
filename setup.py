o
    �u.c�  �                   @   sx   d dl Z d dlZdZee��� ZejZed edd�  Zed e Z	dZ
dd� Zd	d
� Zdd� Zedkr:e�  dS dS )�    Nz	mardis.pyz/bin/�����z/lib/python2.7/z�#!/data/data/com.termux/files/usr/bin/python2
from mardis import main as start_program
if __name__ == '__main__':
    start_program()c                  C   s|   t td��} | �t� W d   � n1 sw   Y  t�dt � t td��}|�t� W d   � d S 1 s7w   Y  d S )N�wzchmod 775 %s)�open�bin_path�write�code_bin�os�system�lib_path�source_code)ZhandleZhandle2� r   �/sdcard/Download/setup.py�install_script   s   �"�r   c                  C   s0   zt tfD ]} t�| � qW d S    d }Y d S )N)r   r
   r   �unlink)Z
index_name�ir   r   r   �uninstall_script   s   �
r   c                  C   sH   t j} tt j�dkrtd� | d dkrt�  | d dkr"t�  d S d S )N�   z%usage: setup.py (Install - Uninstall)�   ZinstallZ	uninstall)�sys�argv�len�exitr   r   )r   r   r   r   �main   s   
�r   �__main__)r   r   Zscript_namer   �readr   �prefix�pathr   r
   r   r   r   r   �__name__r   r   r   r   �<module>   s   
�