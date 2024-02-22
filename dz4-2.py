def get_cats_info(path):
    result = []
    try:
        with open(path, "r") as fh:
            lines = fh.readlines()
            for line in lines:
                id, name, age = line.strip().split(",")
                
                result.append({"id":id, "name":name, "age":age})
        return result        
    except FileNotFoundError:
        print("File not found")



get_cats_info("dz42.txt")
    