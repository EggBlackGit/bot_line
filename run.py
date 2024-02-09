import uvicorn

import alembic.config
import src.setting as stg


if __name__ == "__main__":
    alembic.config.main(argv=["upgrade", "head"])
    uvicorn.run(
        "src.main:app",
        host=stg.HOST,
        port=stg.PORT,
        reload=False,
        ws="none",
        log_level="info"
    )