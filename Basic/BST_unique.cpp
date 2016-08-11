/* Implement Binary Search Tree with unique_ptr (c++11)
 * Source:
 * http://stackoverflow.com/questions/24591680/using-unique-ptr-instead-of-shared-ptr-in-bst
 * Explaining the difference from shared_ptr:
 * -----------------------------------------------------------------------
 * `unique_ptrs` are not assignable but moveable. I reworked your example
 * and now works with `unique_ptrs`. Notice, that I use `std::move`
 * in order to move contents from one `unique_ptr` to another. Also due to
 * the fact that `unique_ptr` isn't copyable, I pass unique_ptrs in member
 * functions by reference and not by value.
 * -----------------------------------------------------------------------
 * */

#include <iostream>
#include <memory>

// template parameter pack 
// source:
// http://en.cppreference.com/w/cpp/language/parameter_pack
// TODO: read more about it.
template<class T, class... Args>
std::unique_ptr<T> make_unique(Args&&... args)
{
    return std::unique_ptr<T>(new T(std::forward<Args>(args)...));
}

template<class T>
class BinarySearchTree
{
    struct TreeNode;    // declare the structure of treenode
    typedef std::unique_ptr<TreeNode> spTreeNode;   // use smart pointer
    struct TreeNode
    {
        T data;
        spTreeNode left;
        spTreeNode right;
        TreeNode(const T& value) : data(value), left(nullptr), right(nullptr){}
    };

    spTreeNode root;
    bool insert(spTreeNode &node);          // unique_ptr is not capyable   <-- TODO: check if unused
    void print(const spTreeNode&) const;    // pass by reference not value
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
    //std::unique_ptr<TreeNode> node( new TreeNode(ref));
    std::unique_ptr<TreeNode> node = make_unique<TreeNode>(ref);
    if(root == nullptr)
    {
        root = std::move(node);
    }
    else
    {
        TreeNode* temp = root.get();
        TreeNode* prev = root.get();
        while(temp != nullptr)
        {
            prev = temp;
            if(temp->data < ref)
                temp = temp->right.get();
            else
                temp = temp->left.get();
        }
        if(prev->data < ref)
            prev->right = std::move(node);
        else
            prev->left = std::move(node);
    }
}

template<class T>
void BinarySearchTree<T>::print()const
{
    print(root);
}

template<class T>
void BinarySearchTree<T>::print(const spTreeNode &node)const
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
