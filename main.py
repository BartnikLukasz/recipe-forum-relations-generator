import random
import math


def print_sql_relations(user_size, category_size, recipe_size, comment_size, product_category_size, product_size, line_item_size, order_size):

    user_size += 1
    category_size += 1
    recipe_size += 1
    comment_size += 1
    product_category_size += 1
    product_size += 1
    line_item_size += 1
    order_size += 1

    category = "=Category!D"
    user = "=User!J"
    recipe = "=Recipe!L"
    productCategory = "=ProductCategory!D"
    product = "=Product!G"
    order = "=Order!E"

    recipe_category = ''
    recipe_user = ''
    comment_recipe = ''
    comment_user = ''
    product_product_category = ''
    line_item_product = ''
    line_item_order = ''
    order_user = ''
    liked_recipe_liked_recipe = ''
    liked_recipe_custom_user = ''
    disliked_recipe_disliked_recipe = ''
    disliked_recipe_custom_user = ''

    print("Generating Recipe relations")

    for i in range(recipe_size):
        recipe_category += category + str(random.randint(2, category_size)) + "\n"
        recipe_user += user + str(random.randint(2, user_size)) + "\n"

    print("Generating Comment relations")

    for i in range(comment_size):
        comment_recipe += recipe + str(random.randint(2, recipe_size)) + "\n"
        comment_user += user + str(random.randint(2, user_size)) + "\n"

    print("Generating Product relations")

    for i in range(product_size):
        product_product_category += productCategory + str(random.randint(2, product_category_size)) + "\n"

    print("Generating Line Item relations")

    for i in range(line_item_size):
        line_item_product += product + str(random.randint(2, product_size)) + "\n"
        line_item_order += order + str(random.randint(2, order_size)) + "\n"

    print("Generating Order relations")

    for i in range(order_size):
        order_user += user + str(random.randint(2, user_size)) + "\n"

    print("Generating Liked and Disliked Recipes relations")

    for i in range(2, recipe_size):
        no_users_liking = random.randint(0, math.floor(user_size/2))
        liking_users = random.sample(range(2, user_size), no_users_liking)
        no_users_disliking = random.randint(0, math.floor(user_size/3))
        disliking_users = [x for x in random.sample(range(2, user_size), no_users_disliking) if x not in liking_users]
        for j in range(len(liking_users)):
            liked_recipe_liked_recipe += recipe + str(i) + "\n"
            liked_recipe_custom_user += user + str(liking_users[j]) + "\n"
        for j in range(len(disliking_users)):
            disliked_recipe_disliked_recipe += recipe + str(i) + "\n"
            disliked_recipe_custom_user += user + str(disliking_users[j]) + "\n"

    print("Writing files")

    recipe_category_file = open("sql/recipeCategory.txt", "w")
    recipe_category_file.write(recipe_category)
    recipe_category_file.close()

    recipe_user_file = open("sql/recipeUser.txt", "w")
    recipe_user_file.write(recipe_user)
    recipe_user_file.close()

    comment_recipe_file = open("sql/commentRecipe.txt", "w")
    comment_recipe_file.write(comment_recipe)
    comment_recipe_file.close()

    comment_user_file = open("sql/commentUser.txt", "w")
    comment_user_file.write(comment_user)
    comment_user_file.close()

    product_product_category_file = open("sql/productProductCategory.txt", "w")
    product_product_category_file.write(product_product_category)
    product_product_category_file.close()

    line_item_product_file = open("sql/lineItemProduct.txt", "w")
    line_item_product_file.write(line_item_product)
    line_item_product_file.close()

    line_item_order_file = open("sql/lineItemOrder.txt", "w")
    line_item_order_file.write(line_item_order)
    line_item_order_file.close()

    order_user_file = open("sql/orderUser.txt", "w")
    order_user_file.write(order_user)
    order_user_file.close()

    liked_recipe_liked_recipe_file = open("sql/likedRecipeLikedRecipe.txt", "w")
    liked_recipe_liked_recipe_file.write(liked_recipe_liked_recipe)
    liked_recipe_liked_recipe_file.close()

    liked_recipe_custom_user_file = open("sql/likedRecipeCustomUser.txt", "w")
    liked_recipe_custom_user_file.write(liked_recipe_custom_user)
    liked_recipe_custom_user_file.close()

    disliked_recipe_disliked_recipe_file = open("sql/dislikedRecipeDislikedRecipe.txt", "w")
    disliked_recipe_disliked_recipe_file.write(disliked_recipe_disliked_recipe)
    disliked_recipe_disliked_recipe_file.close()

    disliked_recipe_custom_user_file = open("sql/dislikedRecipeCustomUser.txt", "w")
    disliked_recipe_custom_user_file.write(disliked_recipe_custom_user)
    disliked_recipe_custom_user_file.close()


def print_cypher_relations(user_size, category_size, recipe_size, comment_size, product_category_size, product_size, line_item_size, order_size):

    user_size += 2
    category_size += 2
    recipe_size += 2
    comment_size += 2
    product_category_size += 2
    product_size += 2
    line_item_size += 2
    order_size += 2

    category = "=Category!A"
    user = "=User!A"
    recipe = "=Recipe!A"
    productCategory = "=ProductCategory!A"
    product = "=Product!A"
    order = "=Order!A"

    recipe_category = ''
    recipe_user = ''
    comment_recipe = ''
    comment_user = ''
    product_product_category = ''
    line_item_product = ''
    line_item_order = ''
    order_user = ''
    liked_recipe_liked_recipe = ''
    liked_recipe_custom_user = ''
    disliked_recipe_disliked_recipe = ''
    disliked_recipe_custom_user = ''

    print("Generating Recipe relations")

    for i in range(recipe_size):
        recipe_category += category + str(random.randint(2, category_size)) + "\n"
        recipe_user += user + str(random.randint(2, user_size)) + "\n"

    print("Generating Comment relations")

    for i in range(comment_size):
        comment_recipe += recipe + str(random.randint(2, recipe_size)) + "\n"
        comment_user += user + str(random.randint(2, user_size)) + "\n"

    print("Generating Product relations")

    for i in range(product_size):
        product_product_category += productCategory + str(random.randint(2, product_category_size)) + "\n"

    print("Generating Line Item relations")

    for i in range(line_item_size):
        line_item_product += product + str(random.randint(2, product_size)) + "\n"
        line_item_order += order + str(random.randint(2, order_size)) + "\n"

    print("Generating Order relations")

    for i in range(order_size):
        order_user += user + str(random.randint(2, user_size)) + "\n"

    print("Generating Liked and Disliked Recipes relations")

    for i in range(2, recipe_size):
        no_users_liking = random.randint(0, user_size/2-2)
        liking_users = random.sample(range(2, user_size), no_users_liking)
        no_users_disliking = random.randint(0, user_size/3-2)
        disliking_users = [x for x in random.sample(range(2, user_size), no_users_disliking) if x not in liking_users]
        for j in range(len(liking_users)):
            liked_recipe_liked_recipe += recipe + str(i) + "\n"
            liked_recipe_custom_user += user + str(liking_users[j]) + "\n"
        for j in range(len(disliking_users)):
            disliked_recipe_disliked_recipe += recipe + str(i) + "\n"
            disliked_recipe_custom_user += user + str(disliking_users[j]) + "\n"

    print("Writing files")

    recipe_category_file = open("cypher/recipeCategory.txt", "w")
    recipe_category_file.write(recipe_category)
    recipe_category_file.close()

    recipe_user_file = open("cypher/recipeUser.txt", "w")
    recipe_user_file.write(recipe_user)
    recipe_user_file.close()

    comment_recipe_file = open("cypher/commentRecipe.txt", "w")
    comment_recipe_file.write(comment_recipe)
    comment_recipe_file.close()

    comment_user_file = open("cypher/commentUser.txt", "w")
    comment_user_file.write(comment_user)
    comment_user_file.close()

    product_product_category_file = open("cypher/productProductCategory.txt", "w")
    product_product_category_file.write(product_product_category)
    product_product_category_file.close()

    line_item_product_file = open("cypher/lineItemProduct.txt", "w")
    line_item_product_file.write(line_item_product)
    line_item_product_file.close()

    line_item_order_file = open("cypher/lineItemOrder.txt", "w")
    line_item_order_file.write(line_item_order)
    line_item_order_file.close()

    order_user_file = open("cypher/orderUser.txt", "w")
    order_user_file.write(order_user)
    order_user_file.close()

    liked_recipe_liked_recipe_file = open("cypher/likedRecipeLikedRecipe.txt", "w")
    liked_recipe_liked_recipe_file.write(liked_recipe_liked_recipe)
    liked_recipe_liked_recipe_file.close()

    liked_recipe_custom_user_file = open("cypher/likedRecipeCustomUser.txt", "w")
    liked_recipe_custom_user_file.write(liked_recipe_custom_user)
    liked_recipe_custom_user_file.close()

    disliked_recipe_disliked_recipe_file = open("cypher/dislikedRecipeDislikedRecipe.txt", "w")
    disliked_recipe_disliked_recipe_file.write(disliked_recipe_disliked_recipe)
    disliked_recipe_disliked_recipe_file.close()

    disliked_recipe_custom_user_file = open("cypher/dislikedRecipeCustomUser.txt", "w")
    disliked_recipe_custom_user_file.write(disliked_recipe_custom_user)
    disliked_recipe_custom_user_file.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    user_size = 1000
    category_size = 21
    recipe_size = 1000
    comment_size = 5000
    product_category_size = 10
    product_size = 100
    line_item_size = 300
    order_size = 150

    print_sql_relations(user_size, category_size, recipe_size, comment_size, product_category_size, product_size, line_item_size, order_size)
    # print_cypher_relations(user_size, category_size, recipe_size, comment_size, product_category_size, product_size, line_item_size, order_size)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
