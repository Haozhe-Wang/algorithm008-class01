学习笔记

## 算法题思想

1. 空间换时间
2. 升维
3. 递推或者数学归纳法的思想
4. 由于计算机都是重复性的计算（while，for，recursion） --> 我们就是找问题的重复性
   （找**最近**重复子问题）
   **先找最简单的问题怎么解，然后思考怎么泛化--> 找重复性**
5. 左右夹逼的方法

## 盛最多水容器

应用方法，左右夹逼的方法经常用到！

i，j指向两端。因为最开始宽度最大，之后只要专注于增加高度就好了

## 

```
public int maxArea(int[] height) {
        int vol=0;
        int width,volume,minHeight;
        for ( int i=0, j =height.length-1;i<j;){
            width = j-i;
            minHeight = height[i]>height[j]?height[j--]:height[i++];
            volume = width * minHeight;
            if (vol<volume){vol=volume;}
        }
        return vol;
    }
```



## 爬楼梯

先考虑第一级台阶，然后第二级，第三级。。。。

应用一个递推或者数学归纳法的思想。

**找最近重复子问题：**

**重复性怎么找**： 怎么上第3阶台阶呢？ -->  第2阶台阶上一步，第1阶台阶上2步 （没有第三种方法）

类似于：斐波那契数列

## 3sum

**注意** 是否有重复的元素，以及如果顺序不一样，是否算作同一个元素

简化版： 2sum

一种解法就是记录：用一个hashmap来记录一个值。之后用O(n^2)方法来遍历所有的可能

**优化**

双指针解法：需要数组排序 --> 之所以 2sum不用是因为排序后复杂度更高。但是3sum最快O(n2)就还不错

# 环形链表

[https://leetcode-cn.com/problems/linked-list-cycle/submissions/](https://leetcode-cn.com/problems/linked-list-cycle/submissions/)

**用快慢指针做！快的比慢的能套圈**

