import socket



def get_ip(line):
    # with open('site.txt', 'r') as f:
    #     for line in f:
    #         hostname = line
    hostname = line
    try:
        print(f'Hostname: {hostname}\nIP: {socket.gethostbyname(hostname)}')
    except socket.gaierror as error:
        print(f'{error}')


def main():
    with open('site.txt', 'r') as f:
        for line in f:
            get_ip(line)


if __name__ == '__main__':
    main()
