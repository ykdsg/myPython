import os

from dotenv import load_dotenv
from openai.embeddings_utils import get_embedding, cosine_similarity

import openai

# openai textComplete例子：https://platform.openai.com/docs/quickstart/build-your-application

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

# 获取"好评"和"差评"的向量
positive_review = get_embedding("好评")
negative_review = get_embedding("差评")


def get_score(sample_embedding):
    return cosine_similarity(sample_embedding, positive_review) - cosine_similarity(sample_embedding, negative_review)


def embeddingDemo():
    # 选择使用最小的ada模型
    EMBEDDING_MODEL = "text-embedding-ada-002"

    positive_example = get_embedding(
        "买的银色版真的很好看，一天就到了，晚上就开始拿起来完系统很丝滑流畅，做工扎实，手感细腻，很精致哦苹果一如既往的好品质")
    negative_example = get_embedding("降价厉害，保价不合理，不推荐")

    positive_score = get_score(positive_example)
    negative_score = get_score(negative_example)

    print("好评例子的评分 : %f" % (positive_score))
    print("差评例子的评分 : %f" % (negative_score))

    good_restraurant = get_embedding("这家餐馆太好吃了，一点都不糟糕")
    bad_restraurant = get_embedding("这家餐馆太糟糕了，一点都不好吃")

    good_score = get_score(good_restraurant)
    bad_score = get_score(bad_restraurant)
    print("好评餐馆的评分 : %f" % (good_score))
    print("差评餐馆的评分 : %f" % (bad_score))


if __name__ == '__main__':
    embeddingDemo()
