from benchmark import Benchmark

def main():
    bench = Benchmark()
    while True:
        option = input('1 - Memory \n2 - Reaction \n3 - Chimp')
        if option == '1':
            times = input('quantas vezes?')
            bench.memory(int(times))
        
        if option == '2':
            bench.reaction()
        
        if option == '3':
            times = input('quantas vezes?')
            bench.chimp(int(times))


if __name__ == '__main__':
    main()