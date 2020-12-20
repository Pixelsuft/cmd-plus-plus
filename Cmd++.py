try:
    #imports
    import os
    import subprocess
    import time
    import datetime
    from colorama import init as color_init
    from colorama import Fore, Back, Style
    import pyautogui
    from sys import argv as start_params_mas
    import ctypes
    
    #init
    im_rus=True
    color_init(autoreset=True)
    title_text='Cmd++'
    os.system('title '+title_text)
    print(f'{Back.WHITE}{Fore.BLACK}Pixelsuft CMD++ [Version 1.0]')
    print(f'{Back.WHITE}{Fore.BLACK}(c) Корпорация Пиксельсуфт (Pixelsuft Corporation), 2020. Все права защищены.')
    echo_on=True
    alert_title='Alert!'
    confirm_title='Confirm!'
    prompt_title='prompt!'
    disk_names=['a:','b:','c:','d:','e:','f:','g:','h:','i:','j:','k:','l:','m:','n:','o:','p:','q:','r:','s:','t:','u:','v:','w:','x:','y:','z:']
    
    
    path_bg_color=Back.RED
    path_fg_color=Fore.WHITE
    bg_color=Back.RESET
    #fg_color=Fore.GREEN
    fg_color=Fore.WHITE

    #Functions
    def get_args(command):
        command_split=command.split(' ')
        args=''
        try:
            for i in range(len(command_split)):
                if i==0:
                    args=''
                elif i==1:
                    args=command_split[1]
                else:
                    args+=' '+command_split[i]
            return args
        except:
            return 'error'

    def get_args_mas(command):
        command_split=command.split(' ')
        args=[]
        try:
            for i in range(len(command_split)):
                if i==0:
                    args=[]
                else:
                    args.append(command_split[i])
            return args
        except:
            return 'error'

    def get_args_mas_test(command):
        command_split=command.split(' ')
        args=[]
        for i in range(len(command_split)):
            if i==0:
                args=[]
            else:
                args.append(command_split[i])
        return args

    def replace_env(command):
        env=os.environ
        for i in env:
            command=command.replace('%'+i.lower()+'%',env[i])
            command=command.replace('%'+i.upper()+'%',env[i])
            command=command.replace('%'+i+'%',env[i])
        return command

    #Command
    def send_cmd(command_old):
        command=''
        canfor=True
        for i in command_old:
            if not i==' ':
                canfor=False
            
            if canfor==False:
                command+=i
        command=replace_env(command)
        command_low=command.lower()
        command_split=command.split(' ')
        command_low_split=command_low.split(' ')
        
        result=''
        
        cmd=command_low_split[0]#Make it simple
        
        global title_text
        if get_args(command)=='':
            ctypes.windll.kernel32.SetConsoleTitleW(title_text+' - '+command_split[0])
        else:
            ctypes.windll.kernel32.SetConsoleTitleW(title_text+' - '+command_split[0]+' ('+get_args(command)+')')
        if cmd=='cls' or cmd=='clear':
            print('\033[2J')
        elif cmd=='exit' or  cmd=='quit' or cmd=='close':
            exit()
        elif cmd=='cd' or cmd=='chdir':
            path_to_change=''
            path_to_change_1=''
            path_to_change_2=''
            try:
                for i in range(len(command_split)):
                    if i==0:
                        path_to_change=''
                    elif i==1:
                        path_to_change=command_split[1]
                    else:
                        path_to_change+=' '+command_split[i]
                path_to_change_1=path_to_change.replace('"','')
                path_to_change_2=path_to_change_1.replace("'",'')
                os.chdir(path_to_change_2)
                result=path_to_change_2
            except:
                if path_to_change_2=='':
                    if cmd=='cd':
                        print(f'cd {path_bg_color}{path_fg_color}"path-to-change"{Style.RESET_ALL}')
                    elif cmd=='chdir':
                        print(f'chdir {path_bg_color}{path_fg_color}"path-to-change"{Style.RESET_ALL}')
                else:
                    print(f'Path {path_to_change_2} is not exists!')
        elif cmd=='whoami':
            print(os.getlogin())
            result=os.getlogin()
        elif cmd=='print' or cmd=='echo':
            msg_text=get_args(command)
            if msg_text=='':
                print(f'echo {path_bg_color}{path_fg_color}text-to-show{Style.RESET_ALL}')
            else:
                print(msg_text)
        elif cmd=='dir':
            files=[]
            path=''
            if get_args(command)=='':
                path='.'
            else:
                path=get_args(command).replace('"','').replace("'","").replace('\\','/')
                if not path[-1]=='/':
                    path=path+'/'
            print('path')
            try:
                files=os.listdir(path)
                for i in files:
                    print(i)
                    result+=i
            except:
                print(f'Path not {path_bg_color}{path_fg_color}{path[:len(path)-1]}{Style.RESET_ALL} found')
        elif cmd=='scandir':
            args=get_args(command)
            if args=='':
                os.system('dir')
            else:
                os.system('dir '+args)
        elif cmd=='exec':
            args=get_args(command)
            args=args.replace('"','')
            args=args.replace("'","")
            print(args)
        elif cmd=='@echo':
            global echo_on
            if 'on' in command_low_split:
                echo_on=True
                result='on'
            elif 'off' in command_low_split:
                echo_on=False
                result='off'
        elif cmd=='alert':
            global alert_title
            result=pyautogui.alert(get_args(command), alert_title)
        elif cmd=='alert_title':
            alert_title=get_args(command)
        elif cmd=='confirm':
            global confirm_title
            result=pyautogui.confirm(get_args(command), confirm_title)
        elif cmd=='confirm_title':
            confirm_title=get_args(command)
        elif cmd=='cat':
            path=[]
            show_name=False
            if get_args(command)=='':
                show_name=True
                i=0
                while True:
                    a=input(f'Path [{i}]: ')
                    if a=='':
                        break
                    else:
                        path.append(a)
                    i+=1
            else:
                path=get_args_mas_test(command)
            for i in path:
                if show_name==True:
                    print(f'{i}:')
                try:
                    f=open(f'{i}','r')
                    for j in f.readlines():
                        fx=j.replace("\n","")
                        print(f'{fx}')
                        if result=='':
                            result=fx
                        else:
                            result+='\n'+fx
                    f.close()
                except:
                    print(f'{Back.RED}Error: Failed to open "{i}"{Style.RESET_ALL}')
        elif cmd=='set':
            args_set=get_args_mas(command.replace('=',' '))
            if get_args(command).replace('"','').replace("'","")=='':
                print(f'set {path_bg_color}{path_fg_color}name{Style.RESET_ALL}={path_bg_color}{path_fg_color}value{Style.RESET_ALL}')
            else:
                try:
                    args_mas=get_args_mas(command.replace("="," "))
                    name_env=args_mas[0]
                    value_env=''
                    for i in range(len(args_mas)):
                        if i==0:
                            value_env=''
                        elif i==1:
                            value_env=args_mas[1]
                        else:
                            value_env+=' '+args_mas[i]
                    
                    send_cmd(value_env)
                    
                    os.environ[name_env]=os.environ['__CMD_PLUS_PLUS_RESULT']
                except:
                    print(f'set {path_bg_color}{path_fg_color}name{Style.RESET_ALL}={path_bg_color}{path_fg_color}value{Style.RESET_ALL}')
        elif cmd=='remove_set':
            if get_args(command).replace('"','').replace("'","")=='':
                print(f'remove_set {path_bg_color}{path_fg_color}name{Style.RESET_ALL}')
            else:
                os.environ[get_args(command)]=''
        elif cmd=='ver' or cmd=='version':
            os.system('ver')
            print(f'{Back.WHITE}{Fore.BLACK}Pixelsuft CMD++ [Version 1.0]')
            print(f'{Back.WHITE}{Fore.BLACK}(c) Корпорация Пиксельсуфт (Pixelsuft Corporation), 2020. Все права защищены.')
        elif cmd=='sync':
            result=f'{subprocess.check_output(get_args(command), shell=True)}'
        elif cmd=='color':
            pass
        elif cmd=='str' or cmd=='string':
            result=get_args(command)
        elif cmd=='input':
            result=input('')
        elif cmd=='title':
            title_text=get_args(command)
            if title_text=='':
                print(f'title {path_bg_color}{path_fg_color}application-title-here{Style.RESET_ALL}')
                title_text='Cmd++'
        elif cmd=='':
            pass
        elif cmd in disk_names:
            send_cmd('cd '+ cmd)
        elif cmd=='batrun':
            path_to_file=get_args(command)
            path_to_file=path_to_file.replace('"','')
            path_to_file=path_to_file.replace("'","")
            check_ends=path_to_file.split('.')
            type=check_ends[len(check_ends)-1]
            if type=='cmd' or type=='bat' or type=='sh' or type=='cmdpp':
                try:
                    file_read=open(path_to_file,'r')
                    text=file_read.read().split('\n')
                    before_echo=echo_on
                    i=0
                    while i<len(text):
                        if text[i].split(' ')[0]=='goto':
                            j=0
                            while j<len(text):
                                if text[j]==':'+get_args(text[i]):
                                    i=j
                                    break
                                j+=1
                        else:
                            send_cmd(text[i])
                        i+=1
                    file_read.close()
                    echo_on=before_echo
                except:
                    print(f'File {path_bg_color}{path_fg_color}{path_to_file}{Style.RESET_ALL} is not exists!')
        else:
            path_to_file=command
            path_to_file=path_to_file.replace('"','')
            path_to_file=path_to_file.replace("'","")
            check_ends=path_to_file.split('.')
            type=check_ends[len(check_ends)-1]
            if type=='cmd' or type=='bat' or type=='sh' or type=='cmdpp':
                send_cmd('batrun '+path_to_file)
            else:
                os.system(command)
        os.environ['__CMD_PLUS_PLUS_RESULT']=result

    #On start
    if len(start_params_mas)>1:
        start_params=''
        firt=True
        seond=False
        for i in start_params_mas:
            if firt==True:
                firt=False
                seond=True
            elif seond==True:
                seond=False
                start_params=i
            else:
                start_params+=' '+i
        inputed=start_params.split('&')
        for command in inputed:
            if not command=='':
                send_cmd(command)

    #Main Loop
    while True:
        ctypes.windll.kernel32.SetConsoleTitleW(title_text)
        where_me=os.getcwd().replace('\\','/')
        split_path=where_me.split('/')
        splited_path=''
        try:
            for i in range(3):
                splited_path+=split_path[i]
            for_check='C:Users'+os.getlogin()
            for_while_1=3
            while for_while_1<=len(split_path)-1:
                if for_while_1==3:
                    where_me=split_path[for_while_1]
                else:
                    where_me+='/'+split_path[for_while_1]
                for_while_1+=1
        except:
            split_path=[]
            splited_path=''
        inputed_all=''
        if echo_on==True:
            inputed_all=input(path_bg_color+path_fg_color+where_me+">>"+bg_color+fg_color)
        else:
            inputed_all=input()
        inputed=inputed_all.split('&')
        
        for command in inputed:
            if not command=='':
                send_cmd(command)
except KeyboardInterrupt:
    print('\nCtrl+C Pressed, quiting...')