def process_item(items, position):
    return items[position]  

def main():
    data = ["a", "b", "c"]
    result = process_item(data, 5)  
    assert result == "unknown"
    
main()
