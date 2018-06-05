### 训练
   - 准备训练文件
   ```
   1、进入E:/el目录
   2、将E:/el/el_data/0_good下的所有文件copy到E:/el/data_step1/0_good
   3、将E:/el/el_data/5_duanlu下的所有文件copy到E:/el/data_step1/5_duanlu
   4、将E:/el/el_data/下的所有子文件夹（除去0_good、5_duanlu、14_uncertain）中的文件 copy到E:/el/data_step1/13_bad
   --------------------------------------------------------------------------------------------------------------
   5、将E:/el/el_data/1_liefeng 下的所有文件copy到E:/el/data_step2/1_liefeng
   6、将E:/el/el_data/2_quejiao 下的所有文件copy到E:/el/data_step2/2_quejiao
   7、将E:/el/el_data/7_heixinheiban 下的所有文件copy到E:/el/data_step2/7_heixinheiban
   8、将E:/el/el_data/11_liangban 下的所有文件copy到E:/el/data_step2/11_liangban
   ```
   
   - 训练（anaconda promt环境）
   ```
   $ cd E:/el
   $ python ./retrain.py --bottleneck_dir bottleneck --how_many_training_steps 4000 --model_dir model --output_graph el_graph_1.pb --output_labels el_labels_1.txt --image_dir data_step1 --saved_model_dir ./saved_models/1/
   
   $ python ./retrain.py --bottleneck_dir bottleneck --how_many_training_steps 4000 --model_dir model --output_graph el_graph_2.pb --output_labels el_labels_2.txt --image_dir data_step2 --saved_model_dir ./saved_models/2/
```
