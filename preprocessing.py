from config import logger

def process_data(emp_df, dept_df):

    logger.info("Joining employee and department data")

    final_df = emp_df.merge(
        dept_df,
        on="dept_id",
        how="left"
    )

    final_df["salary"] = final_df["salary"].fillna(0)

    final_df.drop_duplicates(inplace=True)

    logger.info(
        f"Final records after preprocessing: {len(final_df)}"
    )

    return final_df