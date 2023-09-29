import os

# Specify the directory where your images are located
directory = "C:\\Users\\aryuemaan\\Videos\\Speed_Bumps_and_Traffic_Light\\Traffic_light_2"

# Iterate through the files in the directory
for idx, filename in enumerate(os.listdir(directory)):
    if filename.endswith(".jpg"):  # Adjust the file extension if necessary
        new_name = os.path.join(directory, f"image_{idx + 128}.jpg")
        old_path = os.path.join(directory, filename)
        os.rename(old_path, new_name)
        print(f"Renamed {filename} to {new_name}")
