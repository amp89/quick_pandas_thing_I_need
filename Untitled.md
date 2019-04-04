

```python
import pandas as pd
```


```python
item_list = [
        {"name":"a","type_id":"111","stuff":"original_things"},
        {"name":"a2","type_id":"111","stuff":"original_diff_things"},
        {"name":"b","type_id":"222","stuff":"original_things"},
        {"name":"c","type_id":"333","stuff":None},
        {"name":"d","type_id":"444","stuff":"original_other_things"},
        {"name":"e","type_id":"444","stuff":"original_things"},
        {"name":"f","type_id":"555","stuff":"original_things"},
        {"name":"g","type_id":"666","stuff":"original_things"},
        {"name":"h","type_id":"777","stuff":"original_things"},
        
]

stuff_list = [

    {"type_id":"222","stuff":"222right_thing"},
    {"type_id":"222","stuff":"222right_thing"},
    {"type_id":"222","stuff":"222right_thing"},
    {"type_id":"222","stuff":"222right_thing"},
    {"type_id":"222","stuff":"222other_right_thing"},
    {"type_id":"222","stuff":"222other_right_thing"},
    {"type_id":"222","stuff":"222other_right_thing"},
    {"type_id":"222","stuff":"222other_right_thing"},
    {"type_id":"111","stuff":"111wrong_thing"},
    {"type_id":"111","stuff":"111right_thing"},
    {"type_id":"111","stuff":"111right_thing"},
    {"type_id":"000","stuff":"000right_thing"},
    {"type_id":"000","stuff":"000right_thing"},
    {"type_id":"000","stuff":"000right_thing"},
    {"type_id":"444","stuff":"444AA"},
    {"type_id":"555","stuff":None},
    {"type_id":"666","stuff":None},
    {"type_id":"333","stuff":None},
    {"type_id":"333","stuff":"333right_thing"},
    {"type_id":"333","stuff":"333right_thing"},
    {"type_id":"333","stuff":"333right_thing"},
    {"type_id":"333","stuff":"nonsense"},
    {"type_id":"333","stuff":"333right_thing"},
    {"type_id":"333","stuff":"333right_thing"},
    {"type_id":"333","stuff":"333wrong_thing"},
    {"type_id":"333","stuff":"333right_thing"},    
    
]

```


```python
item_df = pd.DataFrame(item_list)
stuff_df = pd.DataFrame(stuff_list)
```


```python
item_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>stuff</th>
      <th>type_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>original_things</td>
      <td>111</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a2</td>
      <td>original_diff_things</td>
      <td>111</td>
    </tr>
    <tr>
      <th>2</th>
      <td>b</td>
      <td>original_things</td>
      <td>222</td>
    </tr>
    <tr>
      <th>3</th>
      <td>c</td>
      <td>None</td>
      <td>333</td>
    </tr>
    <tr>
      <th>4</th>
      <td>d</td>
      <td>original_other_things</td>
      <td>444</td>
    </tr>
    <tr>
      <th>5</th>
      <td>e</td>
      <td>original_things</td>
      <td>444</td>
    </tr>
    <tr>
      <th>6</th>
      <td>f</td>
      <td>original_things</td>
      <td>555</td>
    </tr>
    <tr>
      <th>7</th>
      <td>g</td>
      <td>original_things</td>
      <td>666</td>
    </tr>
    <tr>
      <th>8</th>
      <td>h</td>
      <td>original_things</td>
      <td>777</td>
    </tr>
  </tbody>
</table>
</div>




```python
stuff_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>stuff</th>
      <th>type_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>222right_thing</td>
      <td>222</td>
    </tr>
    <tr>
      <th>1</th>
      <td>222right_thing</td>
      <td>222</td>
    </tr>
    <tr>
      <th>2</th>
      <td>222right_thing</td>
      <td>222</td>
    </tr>
    <tr>
      <th>3</th>
      <td>222right_thing</td>
      <td>222</td>
    </tr>
    <tr>
      <th>4</th>
      <td>222other_right_thing</td>
      <td>222</td>
    </tr>
    <tr>
      <th>5</th>
      <td>222other_right_thing</td>
      <td>222</td>
    </tr>
    <tr>
      <th>6</th>
      <td>222other_right_thing</td>
      <td>222</td>
    </tr>
    <tr>
      <th>7</th>
      <td>222other_right_thing</td>
      <td>222</td>
    </tr>
    <tr>
      <th>8</th>
      <td>111wrong_thing</td>
      <td>111</td>
    </tr>
    <tr>
      <th>9</th>
      <td>111right_thing</td>
      <td>111</td>
    </tr>
    <tr>
      <th>10</th>
      <td>111right_thing</td>
      <td>111</td>
    </tr>
    <tr>
      <th>11</th>
      <td>000right_thing</td>
      <td>000</td>
    </tr>
    <tr>
      <th>12</th>
      <td>000right_thing</td>
      <td>000</td>
    </tr>
    <tr>
      <th>13</th>
      <td>000right_thing</td>
      <td>000</td>
    </tr>
    <tr>
      <th>14</th>
      <td>444AA</td>
      <td>444</td>
    </tr>
    <tr>
      <th>15</th>
      <td>None</td>
      <td>555</td>
    </tr>
    <tr>
      <th>16</th>
      <td>None</td>
      <td>666</td>
    </tr>
    <tr>
      <th>17</th>
      <td>None</td>
      <td>333</td>
    </tr>
    <tr>
      <th>18</th>
      <td>333right_thing</td>
      <td>333</td>
    </tr>
    <tr>
      <th>19</th>
      <td>333right_thing</td>
      <td>333</td>
    </tr>
    <tr>
      <th>20</th>
      <td>333right_thing</td>
      <td>333</td>
    </tr>
    <tr>
      <th>21</th>
      <td>nonsense</td>
      <td>333</td>
    </tr>
    <tr>
      <th>22</th>
      <td>333right_thing</td>
      <td>333</td>
    </tr>
    <tr>
      <th>23</th>
      <td>333right_thing</td>
      <td>333</td>
    </tr>
    <tr>
      <th>24</th>
      <td>333wrong_thing</td>
      <td>333</td>
    </tr>
    <tr>
      <th>25</th>
      <td>333right_thing</td>
      <td>333</td>
    </tr>
  </tbody>
</table>
</div>




```python
stuff_id_map_df = stuff_df.groupby(["type_id","stuff"]).size().sort_values(ascending=False).reset_index().drop_duplicates(subset="type_id")
```


```python
stuff_id_map_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>type_id</th>
      <th>stuff</th>
      <th>0</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>333</td>
      <td>333right_thing</td>
      <td>6</td>
    </tr>
    <tr>
      <th>1</th>
      <td>222</td>
      <td>222right_thing</td>
      <td>4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>000</td>
      <td>000right_thing</td>
      <td>3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>111</td>
      <td>111right_thing</td>
      <td>2</td>
    </tr>
    <tr>
      <th>5</th>
      <td>444</td>
      <td>444AA</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
merged_items = pd.merge(item_df, stuff_id_map_df, how="left", on="type_id")
```


```python
merged_items
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>stuff_x</th>
      <th>type_id</th>
      <th>stuff_y</th>
      <th>0</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>original_things</td>
      <td>111</td>
      <td>111right_thing</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a2</td>
      <td>original_diff_things</td>
      <td>111</td>
      <td>111right_thing</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>b</td>
      <td>original_things</td>
      <td>222</td>
      <td>222right_thing</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>c</td>
      <td>None</td>
      <td>333</td>
      <td>333right_thing</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>d</td>
      <td>original_other_things</td>
      <td>444</td>
      <td>444AA</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>e</td>
      <td>original_things</td>
      <td>444</td>
      <td>444AA</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>f</td>
      <td>original_things</td>
      <td>555</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>g</td>
      <td>original_things</td>
      <td>666</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>h</td>
      <td>original_things</td>
      <td>777</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
merged_items.loc[merged_items["stuff_x"].isnull(), "stuff_x"] = merged_items["stuff_y"] 
```


```python
merged_items
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>stuff_x</th>
      <th>type_id</th>
      <th>stuff_y</th>
      <th>0</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>original_things</td>
      <td>111</td>
      <td>111right_thing</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a2</td>
      <td>original_diff_things</td>
      <td>111</td>
      <td>111right_thing</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>b</td>
      <td>original_things</td>
      <td>222</td>
      <td>222right_thing</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>c</td>
      <td>333right_thing</td>
      <td>333</td>
      <td>333right_thing</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>d</td>
      <td>original_other_things</td>
      <td>444</td>
      <td>444AA</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>e</td>
      <td>original_things</td>
      <td>444</td>
      <td>444AA</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>f</td>
      <td>original_things</td>
      <td>555</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>g</td>
      <td>original_things</td>
      <td>666</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>h</td>
      <td>original_things</td>
      <td>777</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
# df.drop('column_name', axis=1, inplace=True)
merged_items.drop(["stuff_y",0], axis=1, inplace=True)
```


```python
merged_items
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>stuff_x</th>
      <th>type_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>original_things</td>
      <td>111</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a2</td>
      <td>original_diff_things</td>
      <td>111</td>
    </tr>
    <tr>
      <th>2</th>
      <td>b</td>
      <td>original_things</td>
      <td>222</td>
    </tr>
    <tr>
      <th>3</th>
      <td>c</td>
      <td>333right_thing</td>
      <td>333</td>
    </tr>
    <tr>
      <th>4</th>
      <td>d</td>
      <td>original_other_things</td>
      <td>444</td>
    </tr>
    <tr>
      <th>5</th>
      <td>e</td>
      <td>original_things</td>
      <td>444</td>
    </tr>
    <tr>
      <th>6</th>
      <td>f</td>
      <td>original_things</td>
      <td>555</td>
    </tr>
    <tr>
      <th>7</th>
      <td>g</td>
      <td>original_things</td>
      <td>666</td>
    </tr>
    <tr>
      <th>8</th>
      <td>h</td>
      <td>original_things</td>
      <td>777</td>
    </tr>
  </tbody>
</table>
</div>




```python
merged_items.rename(columns={"stuff_x":"stuff"})
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>stuff</th>
      <th>type_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>original_things</td>
      <td>111</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a2</td>
      <td>original_diff_things</td>
      <td>111</td>
    </tr>
    <tr>
      <th>2</th>
      <td>b</td>
      <td>original_things</td>
      <td>222</td>
    </tr>
    <tr>
      <th>3</th>
      <td>c</td>
      <td>333right_thing</td>
      <td>333</td>
    </tr>
    <tr>
      <th>4</th>
      <td>d</td>
      <td>original_other_things</td>
      <td>444</td>
    </tr>
    <tr>
      <th>5</th>
      <td>e</td>
      <td>original_things</td>
      <td>444</td>
    </tr>
    <tr>
      <th>6</th>
      <td>f</td>
      <td>original_things</td>
      <td>555</td>
    </tr>
    <tr>
      <th>7</th>
      <td>g</td>
      <td>original_things</td>
      <td>666</td>
    </tr>
    <tr>
      <th>8</th>
      <td>h</td>
      <td>original_things</td>
      <td>777</td>
    </tr>
  </tbody>
</table>
</div>


