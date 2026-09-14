; ModuleID = 'algorithms/02_c/sorting/merge_sort.c'
source_filename = "algorithms/02_c/sorting/merge_sort.c"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: nounwind sspstrong memory(readwrite, target_mem0: none, target_mem1: none) uwtable
define dso_local void @merge(ptr noundef captures(none) %0, i32 noundef %1, i32 noundef %2, i32 noundef %3) local_unnamed_addr #0 {
  %5 = sub nsw i32 %2, %1
  %6 = add nsw i32 %5, 1
  %7 = sub nsw i32 %3, %2
  %8 = sext i32 %6 to i64
  %9 = shl nsw i64 %8, 2
  %10 = tail call noalias ptr @malloc(i64 noundef %9) #6
  %11 = sext i32 %7 to i64
  %12 = shl nsw i64 %11, 2
  %13 = tail call noalias ptr @malloc(i64 noundef %12) #6
  %14 = icmp slt i32 %5, 0
  br i1 %14, label %23, label %15

15:                                               ; preds = %4
  %16 = sext i32 %1 to i64
  %17 = shl nsw i64 %16, 2
  %18 = getelementptr i8, ptr %0, i64 %17
  %19 = add i32 %2, 1
  %20 = sub i32 %19, %1
  %21 = zext i32 %20 to i64
  %22 = shl nuw nsw i64 %21, 2
  tail call void @llvm.memcpy.p0.p0.i64(ptr align 4 %10, ptr align 4 %18, i64 %22, i1 false), !tbaa !5
  br label %23

23:                                               ; preds = %15, %4
  %24 = icmp sgt i32 %7, 0
  br i1 %24, label %25, label %61

25:                                               ; preds = %23
  %26 = zext nneg i32 %7 to i64
  %27 = sext i32 %2 to i64
  %28 = getelementptr i32, ptr %0, i64 %27
  %29 = icmp ult i32 %7, 8
  br i1 %29, label %45, label %30

30:                                               ; preds = %25
  %31 = and i64 %26, 2147483640
  br label %32

32:                                               ; preds = %32, %30
  %33 = phi i64 [ 0, %30 ], [ %41, %32 ]
  %34 = getelementptr i32, ptr %28, i64 %33
  %35 = getelementptr i8, ptr %34, i64 4
  %36 = getelementptr i8, ptr %34, i64 20
  %37 = load <4 x i32>, ptr %35, align 4, !tbaa !5
  %38 = load <4 x i32>, ptr %36, align 4, !tbaa !5
  %39 = getelementptr inbounds nuw i32, ptr %13, i64 %33
  %40 = getelementptr inbounds nuw i8, ptr %39, i64 16
  store <4 x i32> %37, ptr %39, align 4, !tbaa !5
  store <4 x i32> %38, ptr %40, align 4, !tbaa !5
  %41 = add nuw i64 %33, 8
  %42 = icmp eq i64 %41, %31
  br i1 %42, label %43, label %32, !llvm.loop !9

43:                                               ; preds = %32
  %44 = icmp eq i64 %31, %26
  br i1 %44, label %47, label %45

45:                                               ; preds = %25, %43
  %46 = phi i64 [ 0, %25 ], [ %31, %43 ]
  br label %51

47:                                               ; preds = %51, %43
  %48 = icmp sgt i32 %5, -1
  br i1 %48, label %49, label %61

49:                                               ; preds = %47
  %50 = sext i32 %1 to i64
  br label %102

51:                                               ; preds = %45, %51
  %52 = phi i64 [ %57, %51 ], [ %46, %45 ]
  %53 = getelementptr i32, ptr %28, i64 %52
  %54 = getelementptr i8, ptr %53, i64 4
  %55 = load i32, ptr %54, align 4, !tbaa !5
  %56 = getelementptr inbounds nuw i32, ptr %13, i64 %52
  store i32 %55, ptr %56, align 4, !tbaa !5
  %57 = add nuw nsw i64 %52, 1
  %58 = icmp eq i64 %57, %26
  br i1 %58, label %47, label %51, !llvm.loop !13

59:                                               ; preds = %102
  %60 = trunc nsw i64 %119 to i32
  br label %61

61:                                               ; preds = %23, %59, %47
  %62 = phi i32 [ 0, %47 ], [ %114, %59 ], [ 0, %23 ]
  %63 = phi i32 [ 0, %47 ], [ %117, %59 ], [ 0, %23 ]
  %64 = phi i32 [ %1, %47 ], [ %60, %59 ], [ %1, %23 ]
  %65 = icmp sgt i32 %62, %5
  br i1 %65, label %127, label %66

66:                                               ; preds = %61
  %67 = sext i32 %64 to i64
  %68 = shl nsw i64 %67, 2
  %69 = getelementptr i8, ptr %0, i64 %68
  %70 = zext nneg i32 %62 to i64
  %71 = shl nuw nsw i64 %70, 2
  %72 = getelementptr i8, ptr %10, i64 %71
  %73 = add i32 %62, %1
  %74 = sub i32 %2, %73
  %75 = zext i32 %74 to i64
  %76 = shl nuw nsw i64 %75, 2
  %77 = add nuw nsw i64 %76, 4
  tail call void @llvm.memcpy.p0.p0.i64(ptr noundef nonnull align 4 dereferenceable(1) %69, ptr noundef nonnull align 4 dereferenceable(1) %72, i64 %77, i1 false), !tbaa !5
  %78 = add i32 %2, 1
  %79 = sub i32 %78, %1
  %80 = zext i32 %79 to i64
  %81 = sub nsw i64 %80, %70
  %82 = icmp ult i64 %81, 4
  br i1 %82, label %99, label %83

83:                                               ; preds = %66
  %84 = and i64 %81, -4
  %85 = add nsw i64 %84, %70
  %86 = insertelement <2 x i64> <i64 poison, i64 0>, i64 %67, i64 0
  br label %87

87:                                               ; preds = %87, %83
  %88 = phi i64 [ 0, %83 ], [ %93, %87 ]
  %89 = phi <2 x i64> [ %86, %83 ], [ %91, %87 ]
  %90 = phi <2 x i64> [ zeroinitializer, %83 ], [ %92, %87 ]
  %91 = add <2 x i64> %89, splat (i64 1)
  %92 = add <2 x i64> %90, splat (i64 1)
  %93 = add nuw i64 %88, 4
  %94 = icmp eq i64 %93, %84
  br i1 %94, label %95, label %87, !llvm.loop !14

95:                                               ; preds = %87
  %96 = add <2 x i64> %92, %91
  %97 = tail call i64 @llvm.vector.reduce.add.v2i64(<2 x i64> %96)
  %98 = icmp eq i64 %81, %84
  br i1 %98, label %124, label %99

99:                                               ; preds = %66, %95
  %100 = phi i64 [ %70, %66 ], [ %85, %95 ]
  %101 = phi i64 [ %67, %66 ], [ %97, %95 ]
  br label %143

102:                                              ; preds = %49, %102
  %103 = phi i64 [ %50, %49 ], [ %119, %102 ]
  %104 = phi i32 [ 0, %49 ], [ %117, %102 ]
  %105 = phi i32 [ 0, %49 ], [ %114, %102 ]
  %106 = zext nneg i32 %105 to i64
  %107 = getelementptr inbounds nuw i32, ptr %10, i64 %106
  %108 = load i32, ptr %107, align 4, !tbaa !5
  %109 = zext nneg i32 %104 to i64
  %110 = getelementptr inbounds nuw i32, ptr %13, i64 %109
  %111 = load i32, ptr %110, align 4, !tbaa !5
  %112 = icmp sle i32 %108, %111
  %113 = zext i1 %112 to i32
  %114 = add nuw nsw i32 %105, %113
  %115 = xor i1 %112, true
  %116 = zext i1 %115 to i32
  %117 = add nuw nsw i32 %104, %116
  %118 = tail call i32 @llvm.smin.i32(i32 %108, i32 %111)
  %119 = add nsw i64 %103, 1
  %120 = getelementptr inbounds i32, ptr %0, i64 %103
  store i32 %118, ptr %120, align 4, !tbaa !5
  %121 = icmp sle i32 %114, %5
  %122 = icmp slt i32 %117, %7
  %123 = select i1 %121, i1 %122, i1 false
  br i1 %123, label %102, label %59, !llvm.loop !15

124:                                              ; preds = %143, %95
  %125 = phi i64 [ %97, %95 ], [ %147, %143 ]
  %126 = trunc nsw i64 %125 to i32
  br label %127

127:                                              ; preds = %124, %61
  %128 = phi i32 [ %64, %61 ], [ %126, %124 ]
  %129 = icmp slt i32 %63, %7
  br i1 %129, label %130, label %149

130:                                              ; preds = %127
  %131 = sext i32 %128 to i64
  %132 = shl nsw i64 %131, 2
  %133 = getelementptr i8, ptr %0, i64 %132
  %134 = sext i32 %63 to i64
  %135 = shl nsw i64 %134, 2
  %136 = getelementptr i8, ptr %13, i64 %135
  %137 = xor i32 %63, -1
  %138 = add i32 %3, %137
  %139 = sub i32 %138, %2
  %140 = zext i32 %139 to i64
  %141 = shl nuw nsw i64 %140, 2
  %142 = add nuw nsw i64 %141, 4
  tail call void @llvm.memcpy.p0.p0.i64(ptr noundef nonnull align 4 dereferenceable(1) %133, ptr noundef nonnull align 4 dereferenceable(1) %136, i64 %142, i1 false), !tbaa !5
  br label %149

143:                                              ; preds = %99, %143
  %144 = phi i64 [ %146, %143 ], [ %100, %99 ]
  %145 = phi i64 [ %147, %143 ], [ %101, %99 ]
  %146 = add nuw nsw i64 %144, 1
  %147 = add nsw i64 %145, 1
  %148 = icmp eq i64 %146, %80
  br i1 %148, label %124, label %143, !llvm.loop !16

149:                                              ; preds = %130, %127
  tail call void @free(ptr noundef %10) #7
  tail call void @free(ptr noundef %13) #7
  ret void
}

; Function Attrs: mustprogress nofree nounwind willreturn allockind("alloc,uninitialized") allocsize(0) memory(inaccessiblemem: readwrite)
declare noalias noundef ptr @malloc(i64 noundef) local_unnamed_addr #1

; Function Attrs: mustprogress nounwind willreturn allockind("free") memory(argmem: readwrite, inaccessiblemem: readwrite)
declare void @free(ptr allocptr noundef captures(none)) local_unnamed_addr #2

; Function Attrs: nounwind sspstrong memory(readwrite, target_mem0: none, target_mem1: none) uwtable
define dso_local void @merge_sort(ptr noundef %0, i32 noundef %1, i32 noundef %2) local_unnamed_addr #0 {
  %4 = icmp slt i32 %1, %2
  br i1 %4, label %6, label %5

5:                                                ; preds = %3, %6
  ret void

6:                                                ; preds = %3
  %7 = sub nsw i32 %2, %1
  %8 = lshr i32 %7, 1
  %9 = add nsw i32 %8, %1
  tail call void @merge_sort(ptr noundef %0, i32 noundef %1, i32 noundef %9)
  %10 = add nsw i32 %9, 1
  tail call void @merge_sort(ptr noundef %0, i32 noundef %10, i32 noundef %2)
  tail call void @merge(ptr noundef %0, i32 noundef %1, i32 noundef %9, i32 noundef %2)
  br label %5
}

; Function Attrs: nocallback nocreateundeforpoison nofree nosync nounwind speculatable willreturn memory(none)
declare i32 @llvm.smin.i32(i32, i32) #3

; Function Attrs: nocallback nofree nounwind willreturn memory(argmem: readwrite)
declare void @llvm.memcpy.p0.p0.i64(ptr noalias writeonly captures(none), ptr noalias readonly captures(none), i64, i1 immarg) #4

; Function Attrs: nocallback nofree nosync nounwind speculatable willreturn memory(none)
declare i64 @llvm.vector.reduce.add.v2i64(<2 x i64>) #5

attributes #0 = { nounwind sspstrong memory(readwrite, target_mem0: none, target_mem1: none) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #1 = { mustprogress nofree nounwind willreturn allockind("alloc,uninitialized") allocsize(0) memory(inaccessiblemem: readwrite) "alloc-family"="malloc" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #2 = { mustprogress nounwind willreturn allockind("free") memory(argmem: readwrite, inaccessiblemem: readwrite) "alloc-family"="malloc" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #3 = { nocallback nocreateundeforpoison nofree nosync nounwind speculatable willreturn memory(none) }
attributes #4 = { nocallback nofree nounwind willreturn memory(argmem: readwrite) }
attributes #5 = { nocallback nofree nosync nounwind speculatable willreturn memory(none) }
attributes #6 = { nounwind allocsize(0) }
attributes #7 = { nounwind }

!llvm.module.flags = !{!0, !1, !2, !3}
!llvm.ident = !{!4}
!llvm.errno.tbaa = !{!5}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{i32 8, !"PIC Level", i32 2}
!2 = !{i32 7, !"PIE Level", i32 2}
!3 = !{i32 7, !"uwtable", i32 2}
!4 = !{!"clang version 22.1.8"}
!5 = !{!6, !6, i64 0}
!6 = !{!"int", !7, i64 0}
!7 = !{!"omnipotent char", !8, i64 0}
!8 = !{!"Simple C/C++ TBAA"}
!9 = distinct !{!9, !10, !11, !12}
!10 = !{!"llvm.loop.mustprogress"}
!11 = !{!"llvm.loop.isvectorized", i32 1}
!12 = !{!"llvm.loop.unroll.runtime.disable"}
!13 = distinct !{!13, !10, !12, !11}
!14 = distinct !{!14, !10, !11, !12}
!15 = distinct !{!15, !10}
!16 = distinct !{!16, !10, !12, !11}
