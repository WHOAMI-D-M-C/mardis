o
    �.c  �                
   @   s�   d dl Z d dlZd dlZd dlZd dlZd dlZzd dlZW n ey6 Z ze	e
e�� W Y dZ[ndZ[ww dZe�d�Ze�d�Zdd� Zdd� Zd	d
� Zdd� Zdd� ZG dd� d�Zdd� Zedkrke�  dS dS )�    NZmardisaP  JXMKaW1wb3J0IHVuY29tcHlsZTYsIHN5cwpkZWYgZGVjb21waWxlKHZlcnNpb24sIGNvZGVfb2JqZWN0LCBpbyk6CiAgICB0cnk6CiAgICAgICAgdW5jb21weWxlNi5tYWluLmRlY29tcGlsZSh2ZXJzaW9uLCBjb2RlX29iamVjdCwgaW8pCiAgICBleGNlcHQ6IHByaW50KCJkZWNvbXBpbGUgZXJvcj8iKQppZiBoYXNhdHRyKHNzLCAiY29fY29kZSIpOgogICAgZGVjb21waWxlKDIuNywgc3MsIHN5cy5zdGRvdXQpCmVsc2U6IHByaW50KHNzKQ==ZhIyBEZWNvbXBpbGUgYnkgTWFyZGlzIChUb29scyBCeSBLYXB0ZW4tS2Fpem8pCiMgVGltZSBTdWNjZXMgZGVjb21waWxlIDogJXMKJXMKc                 C   s�   t | ��� }dd� |�� D �}ttj�� �}t|d�|�f }t | dd��}|�|� W d   � n1 s5w   Y  t	d|  � d S )Nc                 S   s   g | ]	}|� d �s|�qS )�#)�
startswith)�.0�line� r   �/sdcard/Download/mardis.py�
<listcomp>   s    zrmbg.<locals>.<listcomp>�
�w)�modez decompiling done!. saved to `%s`)
�open�read�
splitlines�str�datetime�now�	have_code�join�write�exit)�	file_name�rZconsoleZtimestapZresult_codeZsave_disr   r   r   �rmbg   s   �r   c                 C   s@   t | d��}|�|� W d   � n1 sw   Y  t|� d S )Nr
   )r   r   r   )�file�string�messageZindihomer   r   r   �
simpen_cok   s   �r   c              
   C   s8   | � d�dt�d| �d g�d�dt�d| �d g��S )N� �exec�exec(.*)r   zss=)�replacer   �re�findall)�
master_keyr   r   r   �<lambda>   s   8 r$   c              
   C   s�   zt | � W n ty% } zttjd tdt|� � W Y d }~nd }~ww tt�t	j
u r9tdttt�f � d S tdt � d S )N�   zException: %sz%s: %sz%s: No Compile Module given !!)r   �	Exceptionr   �sys�argv�	save_coder   �type�ss�types�CodeType�print�dah_lah)r   �ir   r   r   �	show_info   s   &��r1   c                 C   s  t | ��� }t|�� gd �}|�d�dkr+tj�|�r%t|t	dt
 � ntdt
 � |t� d< |�d�dkrxtt�d|��dkrJt|t	d	t
 � nt|�}t|� t |d
��t| � t�d||f � tj�|�rpt�|� t|||� d S tj�|�r�t|� d S td|  � d S )Nr   zdecompile eror?z%s: Decompile error!z%s: Decompile failed!r)   r   r   r%   z%s: Exec string is biggest!!r
   zpython2 %s > %sz'%s: decompile failed!. not found `exec`)r   r   �lenr   �count�os�path�existsr   r)   �script_namer   �globalsr!   r"   �find_string_execr1   r   �code_marshal�system�unlink�disr   )Z	nama_fileZoutput_fileZ	ekse_filer#   r   Znew_coder   r   r   r=   &   s(   

r=   c                   @   s,   e Zd Zdd� Zdd� Zdd� Zdd� Zd	S )
�Typec                 C   s~   t |�| _|j| _|j| _|j| _|j| _|j| _|j| _|j| _|j	| _	|j
| _
|j| _|j| _|j| _|j| _|j| _d S �N)r   r   �co_argcount�
co_nlocals�co_stacksize�co_flags�co_code�	co_consts�co_names�co_varnames�co_filename�co_name�co_firstlineno�	co_lnotab�co_freevars�co_cellvars)�self�coder   r   r   �__init__=   s   
zType.__init__c                 C   s@   t �| j| j| j| j| j| j| j| j	| j
| j| j| j| j| j�S r?   )r,   r-   r@   rA   rB   rC   rD   rE   rF   rG   rH   rI   rJ   rK   rL   rM   )�cor   r   r   �myasmM   s   @z
Type.myasmc                 C   �   | j S r?   �r   �rN   r   r   r   �__repr__O   �   zType.__repr__c                 C   rS   r?   rT   rU   r   r   r   �__str__Q   rW   zType.__str__N)�__name__�
__module__�__qualname__rP   rR   rV   rX   r   r   r   r   r>   <   s
    r>   c                   C   sR   t tj�dkrtd� tjd t� d< tddgt_tdtjd  � ttj�  d S )N�   zusage: mardis file_name.pyr%   r/   zcode.pyz.master_keyz2If You Get Error Decompile, Error code saved to %s)r2   r'   r(   r   r8   r/   r.   r=   r   r   r   r   �mainS   s   r]   �__main__)r4   r'   r!   r   r,   �base64Z
uncompyle6r&   r0   r   r   r7   �	b64decoder:   r   r   r   r9   r1   r=   r>   r]   rY   r   r   r   r   �<module>   s2   ��


�