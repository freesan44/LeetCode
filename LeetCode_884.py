# 给定两个句子 A 和 B 。 （句子是一串由空格分隔的单词。每个单词仅由小写字母组成。）
#
# 如果一个单词在其中一个句子中只出现一次，在另一个句子中却没有出现，那么这个单词就是不常见的。
#
# 返回所有不常用单词的列表。
#
# 您可以按任何顺序返回列表。
#
#  
#
# 示例
# 1：
#
# 输入：A = "this apple is sweet", B = "this apple is sour"
# 输出：["sweet", "sour"]
# 示例 2：
#
# 输入：A = "apple apple", B = "banana"
# 输出：["banana"]
#  
#
# 提示：
#
# 0 <= A.length <= 200
# 0 <= B.length <= 200
# A
# 和 B 都只包含空格和小写字母。
#
# 来源：力扣（LeetCode）
# 链接：https: // leetcode - cn.com / problems / uncommon - words -
# from
#
# -two - sentences
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> [str]:
        strList = (A+" "+B).split( )
        print(strList)
        import collections
        retDic = collections.Counter(strList)#合并字典，其中数量为1的就是唯一的
        ret = []
        for key in retDic:
           if retDic[key] == 1:
               ret.append(key)
        return ret
if __name__ == '__main__':
    A = "this apple is sweet"
    B = "this apple is sour"
    ret = Solution().uncommonFromSentences(A, B)
    print(ret)