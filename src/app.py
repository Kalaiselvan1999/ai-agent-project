import uvicorn

def main():
    uvicorn.run(
        "main:app",
        reload=True,
        workers=1
    )


if __name__ == "__main__":
    main()