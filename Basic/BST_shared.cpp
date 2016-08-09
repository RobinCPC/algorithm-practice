/* Implement Binary Search Tree with shared_ptr (c++11)
 * Source:
 * http://stackoverflow.com/questions/24591680/using-unique-ptr-instead-of-shared-ptr-in-bst
 * */

#include <iostream>
#include <memory>

template<class T>
class BinarySearchTree
{
    struct TreeNode;    // declare the structure of treenode
    typedef std::shared_ptr<TreeNode> spTreeNode;   // use smart pointer
    struct TreeNode
    {
        T data;
        spTreeNode left;
        spTreeNode right;
        TreeNode(const T& value) : data(value), left(nullptr), right(nullptr){}
    };

    spTreeNode root;
    bool insert(spTreeNode node);       // <-- TODO: check if unused
    void print(const spTreeNode) const;
public:
    BinarySearchTree();     // constructor
    void insert( const T& node);
    void print() const;
};

template<class T>
BinarySearchTree<T>::BinarySearchTree() : root(nullptr){}

template<class T>
void BinarySearchTree<T>::insert(const T& ref)
{
    TreeNode* node = new TreeNode(ref);
    if(root == nullptr)
    {
        root.reset(node);
    }
    else
    {
        spTreeNode temp = root;
        spTreeNode prev = root;
        while(temp != nullptr)
        {
            prev = temp;
            if(temp->data < ref)
                temp = temp->right;
            else
                temp = temp->left;
        }
        if(prev->data < ref)
            prev->right.reset(node);
        else
            prev->left.reset(node);
    }
}

template<class T>
void BinarySearchTree<T>::print()const
{
    print(root);
}

template<class T>
void BinarySearchTree<T>::print(const spTreeNode node)const
{
    if(node == nullptr)
        return;
    print(node->left);
    std::cout << node->data << std::endl;
    print(node->right);
}

int main(void)
{
    BinarySearchTree<int> bst;
    bst.insert(13);
    bst.insert(3);
    bst.insert(5);
    bst.insert(31);
    bst.print();

    return 0;
}
