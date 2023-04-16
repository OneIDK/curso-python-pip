import matplotlib.pyplot as plt

# hacer func pa gráfica
def generate_bar_chart(name, labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig(f'./imgs/{name}.png')
  plt.close()

def gen_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels = labels)
  ax.axis("equal")
  plt.savefig('pie.png')
  plt.close()

def gen_graph_chart():
  plt.plot([1,2,3,4], [1,4,9,16])
  
  plt.ylabel("y numbers")
  plt.xlabel("x numbers")
  
  plt.show()

if __name__ == "__main__":
  values = [630, 420, 480]
  labels = ["momir " + str(values[0] / 60), "estudiar prog " + str(values[1] / 60), "sin registrar " + str(values[2] / 60)]
  #generate_bar_chart(labels, values)
  #gen_pie_chart(labels, values)
  gen_graph_chart()