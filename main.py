from src.Demos import Demos
# "C:\Logiciels\UrbanTerror43"

def main():
    d = Demos("C:\\Logiciels\\UrbanTerror43")

    print(d.initDemosList())
    d.getInfos()


if __name__ == "__main__":
    main()
