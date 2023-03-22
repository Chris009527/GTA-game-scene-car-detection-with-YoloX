import matplotlib.pyplot as plt

train_loss= []


    

    

train_loss.append(3.0)
train_loss.append(2.9)
train_loss.append(2.5)
train_loss.append(2.9)
train_loss.append(2.4)
train_loss.append(2.1)
train_loss.append(2.2)
train_loss.append(2.7)
train_loss.append(2.5)
train_loss.append(2.2)#10
train_loss.append(2.3)
train_loss.append(2.5)
train_loss.append(1.9)
train_loss.append(2.1)
train_loss.append(1.8)
train_loss.append(2.4)
train_loss.append(1.9)
train_loss.append(1.5)
train_loss.append(2.0)
train_loss.append(1.9)#20
train_loss.append(1.7)
train_loss.append(1.7)
train_loss.append(2.3)
train_loss.append(2.3)
train_loss.append(1.9)
train_loss.append(2.0)
train_loss.append(2.0)
train_loss.append(1.8)
train_loss.append(1.6)
train_loss.append(1.9)#30
train_loss.append(1.6)
train_loss.append(1.9)
train_loss.append(2.2)
train_loss.append(2.0)
train_loss.append(1.9)
train_loss.append(1.5)
train_loss.append(1.8)
train_loss.append(2.1)
train_loss.append(1.7)
train_loss.append(1.5)#40
train_loss.append(1.6)
train_loss.append(1.6)
train_loss.append(1.6)
train_loss.append(1.6)
train_loss.append(1.8)
train_loss.append(1.7)
train_loss.append(1.8)
train_loss.append(1.5)
train_loss.append(2.1)
train_loss.append(1.4)#50
train_loss.append(1.8)
train_loss.append(1.5)
train_loss.append(1.5)
train_loss.append(1.9)
train_loss.append(1.9)
train_loss.append(1.6)
train_loss.append(1.1)
train_loss.append(1.1)
train_loss.append(1.9)
train_loss.append(1.6)
train_loss.append(1.3)
train_loss.append(1.7)

 
    

print('\n')
print(f"Training loss: ")


print('-'*50)


# In[23]:


#plot




x1 = range(0, 62)

y1 = train_loss

plt.subplot(2, 1, 2)
plt.plot(x1, y1, '.-')
plt.xlabel('Train loss vs. epoches')
plt.ylabel('Train loss')
plt.show()
#plt.savefig("accuracy_loss.jpg")





se_train_loss= []


    

    

se_train_loss.append(3.7)
se_train_loss.append(2.5)
se_train_loss.append(2.7)
se_train_loss.append(2.4)
se_train_loss.append(2.8)
se_train_loss.append(2.2)
se_train_loss.append(2.0)
se_train_loss.append(2.4)
se_train_loss.append(2.1)
se_train_loss.append(2.0)#10
se_train_loss.append(2.4)
se_train_loss.append(2.2)
se_train_loss.append(2.5)
se_train_loss.append(1.7)
se_train_loss.append(1.7)
se_train_loss.append(2.2)
se_train_loss.append(1.9)
se_train_loss.append(1.7)
se_train_loss.append(1.6)
se_train_loss.append(1.0)#20
se_train_loss.append(0.9)
se_train_loss.append(0.9)
se_train_loss.append(1.0)
se_train_loss.append(0.8)
se_train_loss.append(1.0)
se_train_loss.append(0.8)
se_train_loss.append(1.0)
se_train_loss.append(0.7)
se_train_loss.append(0.9)
se_train_loss.append(0.8)
se_train_loss.append(0.8)
se_train_loss.append(0.8)
se_train_loss.append(0.8)
se_train_loss.append(0.8)
se_train_loss.append(0.6)


print('\n')
print(f"Training loss: ")


print('-'*50)


# In[23]:


#plot




x2 = range(0, 35)

y2 = se_train_loss

plt.subplot(2, 1, 2)
plt.plot(x2, y2, '.-')
plt.xlabel('se Train loss vs. epoches')
plt.ylabel('se Train loss')
plt.show()
#plt.savefig("accuracy_loss.jpg")

