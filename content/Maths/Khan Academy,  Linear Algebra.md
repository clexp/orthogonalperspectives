title: Khan Academy, Linear Algebra, Vectors and spaces
date: 2023-05-16
Modified: 2023-3-4
Tags: #Maths
Slug: 0000003
Authors: clexp
Summary: The mathematical architecture of space.  
Status: draft
Cover: /images/apple-touch-icon_thumb.png


# This was enormous.  

![Default cover image](/images/apple-touch-icon.png)


This was a huge series of mathematical videos. Every video went into depth and detail and worked example.

Every section had multiple subsections and each subsection had multiple videos.

It was an enormous coverage of maths.

It's difficult to know what the value of this was as the depth was quite profound. Often very simple things like addition and subtraction would be covered to some depths, but at a very conceptual or even architectural level. This would inform and provide structure and information that would allow the viewer to compare and connect different areas of maths in their minds. But is it really necessary for machine learning?

I can't tell at this stage.

There is something very beneficial about having a profound knowledge of the basics. It gives you a framework for connecting complexity and simplifying complexity. I can't see from my vantage point at the moment, what the benefit will be. I will just acknowledge that there is benefit as it as it was Riann MacCabe, recommended by Patr here or a series of headings that cover linear algebra.

I have included one or two for Millie, which I think were particularly of note.

# Unit 1 Vectors and spaces
## Vectors
Vectors are values with a direction.  In typical practice this is like a co-ordinate pair $(x,y)$ which you can call a tuple.  
$$\mathbb{R}^2$$This is a set of all 'two-tuples' in 2 dimensional space, 
and we go for broke with:
$$\mathbb{R}^3$$
for 3 dimensional space.  

A scalar will scale up a vector without changing the direction.  
$$3 \begin{bmatrix} 5 \\-7 \\-1\end{bmatrix} =  \begin{bmatrix} 15 \\-21 \\-3\end{bmatrix}$$
And adding is done dimension wise only.  
$$2 \begin{bmatrix} 4 \\3 \\-1\end{bmatrix} + 3 \begin{bmatrix} 5 \\-7 \\-1\end{bmatrix} =  \begin{bmatrix} 23 \\-15 \\-5\end{bmatrix}$$

Scalar will multiply by both values in the vector.

To generalize in n dimensions
$$L = \set{\vec{x}+t\vec{v}|t\in\mathbb{R}}$$
Which is many dimensions for 
$$y=mx+c$$
This leads to parametric representations of lines in N dimensions.  
## Linear combinations and spans
- A linear combination of a 
- A span is that range in space which can be 
This is strictly and linear combination.  
$$2 \begin{bmatrix} 4 \\3 \\-1\end{bmatrix} + 3 \begin{bmatrix} 5 \\-7 \\-1\end{bmatrix} =  \begin{bmatrix} 23 \\-15 \\-5\end{bmatrix}$$
This is a simple scalar multiplication, and simple addition, and this would be called a linear combination.  It is not a vector multiplication.  

Because of this I can represent describe the possible regions we can get to in $\mathbb{R}^2$ with some vectors but not others.  

What is a span?

To pick 2 vectors to cover all $\mathbb{R}^2$ we need value in combinations:
$$\vec{i}=\begin{bmatrix} 1 \\0 \end{bmatrix}; \vec{j}=\begin{bmatrix} 0 \\1 \end{bmatrix}$$
So I can use this to get to span all $\mathbb{R}^2$. 
$$a\vec{i}+ b\vec{j}=a\begin{bmatrix} 1 \\0 \end{bmatrix}+b\begin{bmatrix} 0 \\1\end{bmatrix} = \begin{bmatrix} a \\0 \end{bmatrix}+\begin{bmatrix} 0 \\ b \end{bmatrix}=\begin{bmatrix} a \\ b \end{bmatrix}$$
In the above $i$ and $j$ and linearly independent.  
## Linear dependence and Independence
These terms describe the relationship between vectors.  They may or may not be dependent or independent.  To be linearly independent, none of the set (or pair) of vectors can be expressed as a sum of some multiple of the other vectors.  If they are linearly independent then each of them make a contribution to the vector sum

If you have a set in which some members can be derived from other members then the set is linearly dependent:
$$\set{\begin{bmatrix} 1 \\4 \\2 \end{bmatrix},\begin{bmatrix} 2 \\1 \\3\end{bmatrix},\begin{bmatrix} 0 \\7 \\1\end{bmatrix}}$$
And if the set contains elements that cannot be derived from each other, then they are linearly independent
$$\set{\begin{bmatrix} 1 \\0 \\0 \end{bmatrix},\begin{bmatrix} 0 \\1 \\0\end{bmatrix},\begin{bmatrix} 0 \\0 \\1\end{bmatrix}}$$



## Subspaces and the basis for a subspace
A subspace is a subset of a set.  The key point is that if you take a vector in a subset, and multiply it by a scalar, then you get another vector, also inside the set.  This is called 'closure under multiplication'.  This goes further: if you take 2 vectors that are in your subset, and you add them then you will also end up with a new vector, also inside the set.  This is called 'closure under addition'.  These two features are actually part of the definition of a subspace or of a set.  
<img  src='/images/Maths/Khan_Lin_alg_real_coord_space.jpg'>
The span of any set of numbers is a  valid subspace.  

The span of $n$ vectors is a valid subspace of $\mathbb{R} n$.   

#### 'Basis'
The basis is the minimum set of vectors that spans a subspace.  This set is linearly independent.  
Another set containing the basis plus one vector which is the sum of two vectors in the set is not linearly independent, it is linearly dependent.  

If the set of number is linearly independent, then it is a basis for $\mathbb{R}^2$. (2 dimensional space)
The simplest set of vectors which is a basis for cartesian space or $\mathbb{R}^2$ is 
$$\set{\begin{bmatrix} 1 \\0 \end{bmatrix},\begin{bmatrix} 0 \\1 \end{bmatrix}}$$
and is Linearly independent.  

## Vector dot and cross product
The vector dot product gives us a single number, and is a scalar value. This can be done in any number of dimension, including less than 3.    
The vector cross product gives us a vector.  This can only be done in 3D space, and the vector is always perpendicular to the first two vectors.  (This hurt my head until I could visualize it, then it made sense)

The Cauchy-Schwarz inequality **says the lengths of the dot product of vectors is less than or equal to the product of the lengths of the vectors**. Another form of this inequality says the length of the sum of two vectors is less than or equal to the sum of the lengths of the vectors.

## Matrices for solving systems by elimination

## Null space and column space


# Unit 2 Matrix Transformations
## Functions and Linear Transforms
## Linear Transforms and matrix multiplication
## Inverse Functions and transformations
## Findings inverses and determinants
## More determinant depth
## Transpose of a matrix

# Unit 3 Alternate Coordinate systems
## Orthogonal Complements
## Orthogonal Projections
## Change of basis
## Orthonormal bases and the Gram-Schmidt Process
## Eigen-everything




=====




### Linear dependence and Independence

