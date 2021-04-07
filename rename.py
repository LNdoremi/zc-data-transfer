import os
import json

with open('./pd/issues.json', 'r', encoding='utf-8') as f :
    issue_list = json.load(f)

root = 'C:/Users/LN/Desktop/增城规划院众采/河涌众采导出数据/'
img_root = 'lyzc-1-1259060205.cos.ap-guangzhou.myqcloud.com/'
total = 0
for issue in issue_list:
    issue_id = issue['id']
    town = issue['town']
    address = issue['address']

    pic_paths = issue['pics']
    handle_pic_paths = issue['handlePicList']

    count = 0
    new_pic_paths = list()
    new_handle_pic_paths = list()

    for path in pic_paths:
        src_path = os.path.join(root, path[1:])
        
        if os.path.exists(src_path):
            img_name = '{}_1_{}_{}_{}.jpg'.format(issue_id, town, address, count)
            dst_path = os.path.join(root, 'pd/photos/{}'.format(img_name))
            count += 1
            os.rename(src_path, dst_path)
            new_pic_paths.append('{}{}'.format(img_root, img_name))
        else:
            print('处理前picture not exist: ', src_path)
            print('issue id: ', issue_id)
            
    number = 0

    for path in handle_pic_paths:
        src_path = os.path.join(root, path[1:])
        if os.path.exists(src_path):
            img_name = '{}_2_{}_{}_{}.jpg'.format(issue_id, town, address, number)
            dst_path = os.path.join(root, 'pd/photos/{}'.format(img_name))
            number += 1
            os.rename(src_path, dst_path)
            new_handle_pic_paths.append('{}{}'.format(img_root, img_name))
        else:
            print('处理后picture not exist: ', src_path)
            print('issue id: ', issue_id)
            
    total = total + count + number
    issue['pics'] = new_pic_paths
    issue['handlePicList'] = new_handle_pic_paths

print('valid picture count:', total)
with open('./pd/new_issues.json', 'w', encoding='utf-8') as f :
    json.dump(issue_list, f, ensure_ascii=False)