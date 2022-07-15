from housing.pipeline.pipeline import Pipeline

def main():
    try:
        pipe=Pipeline()
        pipe.run_pipeline()
    except Exception as e:
        print(e)

if __name__=="__main__":
    main()    