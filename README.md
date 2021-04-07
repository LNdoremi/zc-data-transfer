# zc-data-transfer
目标：将旧的河涌众采数据整理成新的河涌众采数据

## 步骤1 
将旧的河涌众采数据导出，应该是图片和Excel的形式


## 步骤2
运行data_process.ipynb

将Excel转换为三个json文件：volunteers.json, issues.json, police.json, 分别代表志愿者表、点位表、巡查员表

## 步骤3
运行rename.py 对图片进行重新命名，生成新的点位表：new_issues.json

