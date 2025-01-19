#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import bpy
import math

def plot_sine_wave(amplitude, frequency, samples, start, end):
    # サイン波の頂点データを生成
    vertices = []
    for i in range(samples):
        x = start + (end - start) * i / (samples - 1)
        y = amplitude * math.sin(frequency * x)
        vertices.append((x, y, 0))
    return vertices

def create_curve(name, vertices):
    # メッシュデータ作成
    mesh = bpy.data.meshes.new(name)
    mesh.from_pydata(vertices, [], [])
    mesh.update()
    
    # オブジェクト作成
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)

if __name__ == '__main__':
    # サイン波の頂点データを生成
    sine_wave_vertices = plot_sine_wave(amplitude=2, frequency=1, samples=100, start=-math.pi, end=math.pi)
    create_curve("SineWave", sine_wave_vertices)

