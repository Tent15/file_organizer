import os
import shutil

def organize_files(directory):
    """
    จัดระเบียบไฟล์ในโฟลเดอร์ที่ระบุโดยย้ายไฟล์ไปยังโฟลเดอร์ย่อยตามนามสกุลของไฟล์
    """
    # ตรวจสอบว่าโฟลเดอร์ที่ระบุมีอยู่จริงหรือไม่
    if not os.path.isdir(directory):
        print(f"ข้อผิดพลาด: ไม่พบโฟลเดอร์ '{directory}'")
        return

    print(f"กำลังจัดระเบียบไฟล์ใน: {directory}")

    # ดึงรายชื่อไฟล์และโฟลเดอร์ทั้งหมดใน directory
    for filename in os.listdir(directory):
        # สร้าง path เต็มของไฟล์
        source_path = os.path.join(directory, filename)

        # ข้ามถ้าหากเป็นโฟลเดอร์
        if os.path.isdir(source_path):
            continue

        # แยกชื่อไฟล์และนามสกุล
        name, extension = os.path.splitext(filename)
        extension = extension[1:]  # ลบจุดหน้าสุดออกจากนามสกุล

        if not extension:
            dest_folder = os.path.join(directory, "Others")
        else:
            dest_folder = os.path.join(directory, extension.upper() + "_Files")

        # สร้างโฟลเดอร์ปลายทางถ้ายังไม่มี
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)
            print(f"สร้างโฟลเดอร์: {dest_folder}")

        # สร้าง path ปลายทางของไฟล์
        destination_path = os.path.join(dest_folder, filename)

        # ย้ายไฟล์
        try:
            shutil.move(source_path, destination_path)
            print(f"ย้าย: {filename} -> {dest_folder}")
        except Exception as e:
            print(f"ไม่สามารถย้ายไฟล์ {filename} ได้: {e}")

    print("\nการจัดระเบียบไฟล์เสร็จสิ้น!")


if __name__ == "__main__":
    target_folder = input("กรุณาใส่ Path ของโฟลเดอร์ที่ต้องการจัดระเบียบ: ")
    
    organize_files(target_folder)