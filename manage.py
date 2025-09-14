import flask
import project


def main():
    try:
        project.project.run(debug = True)
    except Exception as exception:
        print(exception)
        
if __name__ == "__main__":
    main()
